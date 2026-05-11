"""
Step 1: 手写有向图 + channel 驱动的节点遍历（遵循 LangGraph 真实设计）

核心设计（与 LangGraph 源码一致）：
  - 每个节点执行后，返回值写入对应的 channel
  - channel 的值变化触发下游节点的执行
  - compile() 做的事：检查每个节点依赖哪些 channel，
    构建"channel → 下游节点"的触发关系
  - invoke() 按 channel 触发顺序执行节点，不是静态拓扑排序

概念保留：
  - StateGraph  → 手写的 Graph 类
  - START / END → 特殊标记
  - add_node    → dict 添加顶点
  - add_edge    → 构建 channel 触发链
  - compile     → 构建 channel → 节点的触发图
  - invoke      → 触发式遍历，不是静态排序

运行后你会看到：
  1. 邻接表结构
  2. channel 触发链（compile 后构建的内部结构）
  3. 按触发顺序执行节点 A → B → C
"""

from typing import Any, Callable


# ====================================================
# 特殊常量
# ====================================================

START = "__start__"
END = "__end__"


# ====================================================
# 核心实现：channel 驱动的有向图
# ====================================================

class Channel:
    """LangGraph 的 channel 概念 —— 节点之间传递数据的管道。

    每个节点有自己的 channel，节点执行后的返回值写入 channel。
    下游节点监听上游 channel 的变化，被触发后执行。
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.value: Any = None
        self.has_value: bool = False

    def write(self, value: Any) -> None:
        self.value = value
        self.has_value = True

    def read(self) -> Any:
        return self.value

    def __repr__(self) -> str:
        return f"Channel('{self.name}', value={self.value})"


class Graph:
    """手写 LangGraph 内核 —— channel 驱动的有向图执行引擎。

    和 LangGraph 源码一样的设计：
      - add_node: 注册节点函数 + 为它创建对应的 channel
      - add_edge: 建立"上游 channel → 下游节点"的触发关系
      - compile:  构建 channel 到下游节点的映射表（触发图）
      - invoke:   按触发顺序执行节点

    数据结构：
      - nodes:  dict[str, Callable]         节点名 → 节点函数
      - edges:  dict[str, list[str]]        节点名 → 邻接表（出边列表）
      - channels: dict[str, Channel]        节点名 → 对应 channel
      - triggers: dict[str, list[str]]      channel 名 → 被触发的下游节点列表
    """

    def __init__(self) -> None:
        self.nodes: dict[str, Callable[..., Any]] = {}
        self.edges: dict[str, list[str]] = {}
        self.channels: dict[str, Channel] = {}
        # compile 时构建：channel 名 → 它触发的下游节点列表
        self.triggers: dict[str, list[str]] = {}

    def add_node(self, name: str, func: Callable[..., Any]) -> None:
        """注册节点，并为它创建对应的 channel。

        每个节点有自己同名的 channel，节点执行后的返回值
        会写入这个 channel，然后触发下游节点。
        """
        self.nodes[name] = func
        if name not in self.edges:
            self.edges[name] = []
        # 每个节点有自己的 channel（和 LangGraph 一样）
        self.channels[name] = Channel(name)

    def add_edge(self, from_node: str, to_node: str) -> None:
        """添加有向边：from_node → to_node。

        边的语义：from_node 执行后的值，会触发 to_node 执行。
        这是 LangGraph 的核心语义，不是简单的数据流动。
        """
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append(to_node)

    def compile(self) -> "CompiledGraph":
        """构建 channel → 下游节点的触发映射。

        这是 LangGraph compile() 的真实行为：
        遍历所有边，对每条边 A → B：
          - A 执行后值写入 channel_A
          - channel_A 触发 B 执行
        """
        # 构建触发链：每个 channel 触发哪些下游节点
        triggers: dict[str, list[str]] = {}

        for from_node, to_list in self.edges.items():
            # 为每条边 from → to，建立 channel_from → to 的触发关系
            if from_node not in triggers:
                triggers[from_node] = []
            triggers[from_node].extend(to_list)

        # 同时确保所有节点都有 channel 条目（即使是终点）
        all_node_names = set(self.nodes.keys()) | {START, END}
        for name in all_node_names:
            if name not in self.channels:
                self.channels[name] = Channel(name)
            if name not in triggers:
                triggers[name] = []

        return CompiledGraph(
            nodes=self.nodes,
            channels=self.channels,
            triggers=triggers,
            edges=self.edges,
        )


class CompiledGraph:
    """编译后的图 —— 用 channel 触发机制执行节点。

    不依赖静态拓扑排序，而是模拟 LangGraph 的触发执行：
      1. 从 START channel 开始
      2. 写入 START channel 触发第一批节点
      3. 每个节点执行后写入自己的 channel
      4. channel 值变化触发下一批节点
      5. 直到没有节点被触发
    """

    def __init__(
        self,
        nodes: dict[str, Callable[..., Any]],
        channels: dict[str, Channel],
        triggers: dict[str, list[str]],
        edges: dict[str, list[str]],
    ) -> None:
        self.nodes = nodes
        self.channels = channels
        self.triggers = triggers
        self.edges = edges

    def get_graph(self) -> "CompiledGraph":
        """返回自身，和 LangGraph API 一致。"""
        return self

    def invoke(self, initial_state: dict[str, Any]) -> Any:
        """channel 驱动的执行——不是静态拓扑排序。

        执行逻辑：
          1. START channel 先写入初始值
          2. START channel 触发其下游节点
          3. 被触发的节点执行，返回值写入对应 channel
          4. 该 channel 再触发其下游节点
          5. 循环直到所有触发链走完

        这和数据结构课上静态的拓扑排序完全不同——每步是动态触发。
        """
        # 使用队列模拟 channel 触发链
        pending: list[str] = []  # 待执行的节点队列
        executed: set[str] = set()  # 已执行节点（防止重复执行）

        # 检查某个节点的上游 channel 是否都已有值
        def upstream_ready(node_name: str) -> bool:
            """反向查找：所有指向 node_name 的边，其源 channel 都有值了吗？"""
            upstream_channels: list[str] = []
            for src, dst_list in self.edges.items():
                if node_name in dst_list:
                    upstream_channels.append(src)
            if not upstream_channels:
                return True  # 没有上游，直接可以执行
            return all(
                self.channels[ch].has_value for ch in upstream_channels
            )

        print("\n编译后的触发链 (channel → 下游节点)：")
        for ch_name, triggered_nodes in self.triggers.items():
            if triggered_nodes:
                print(f"  Channel[{ch_name}] 触发 → {triggered_nodes}")

        print("\n开始触发式执行：")

        # 手动写入 START channel，触发第一批节点
        start_channel = self.channels[START]
        start_channel.write(initial_state)
        print(f"  ■ Channel[{START}] 写入初始值 → 触发 {self.triggers.get(START, [])}")

        # 将 START 触发的节点加入待执行队列
        for node_name in self.triggers.get(START, []):
            if node_name not in executed and node_name in self.nodes:
                pending.append(node_name)

        # 主循环：channel 驱动的节点执行
        while pending:
            current = pending.pop(0)
            if current in executed:
                continue

            # 检查上游是否就绪
            if not upstream_ready(current):
                # 上游还没准备好，放回队尾等待
                pending.append(current)
                continue

            # 执行节点
            print(f"  → 执行节点 [{current}]")
            result = self.nodes[current](initial_state)

            # 写入 channel
            node_channel = self.channels[current]
            node_channel.write(result)
            print(f"  ■ Channel[{current}] 写入值 → 触发 {self.triggers.get(current, [])}")

            executed.add(current)

            # 该 channel 触发的下游节点加入队列
            for next_node in self.triggers.get(current, []):
                if next_node == END:
                    # END 是特殊标记，不执行
                    end_channel = self.channels[END]
                    end_channel.write(result)
                    print(f"  ■ Channel[{END}] 到达终点")
                    continue
                if next_node not in executed and next_node in self.nodes:
                    pending.append(next_node)

        print(f"\n执行完毕，共执行 {len(executed)} 个节点")
        return self.channels[END].value if self.channels[END].has_value else None


# ====================================================
# 定义节点函数
# ====================================================

def node_a(state: dict[str, Any]) -> dict[str, Any]:
    """节点 A：图的第一个顶点"""
    print("    [A] 执行 node_a")
    return state


def node_b(state: dict[str, Any]) -> dict[str, Any]:
    """节点 B：图的第二个顶点"""
    print("    [B] 执行 node_b")
    return state


def node_c(state: dict[str, Any]) -> dict[str, Any]:
    """节点 C：图的第三个顶点，也是终点"""
    print("    [C] 执行 node_c")
    return state


# ====================================================
# 构建图（和 LangGraph API 完全一致的调用方式）
# ====================================================

graph = Graph()

# 添加顶点
graph.add_node("node_a", node_a)
graph.add_node("node_b", node_b)
graph.add_node("node_c", node_c)

# 添加有向边
graph.add_edge(START, "node_a")    # __start__ → A
graph.add_edge("node_a", "node_b") # A → B
graph.add_edge("node_b", "node_c") # B → C
graph.add_edge("node_c", END)      # C → __end__


# ====================================================
# 编译 + 打印图结构 + 执行
# ====================================================

print("=" * 60)
print("邻接表（手写图结构）：")
print("=" * 60)
for node, neighbors in graph.edges.items():
    print(f"  {node}: {neighbors}")

app = graph.compile()

print("\n" + "=" * 60)
print("执行图（channel 触发式遍历）：")
print("=" * 60)

result = app.invoke({"message": "hello"})
print(f"\n最终结果: {result}")