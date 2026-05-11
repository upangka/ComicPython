"""基于图结构的节点遍历系统

使用深度优先搜索(DFS)算法遍历有向图，每个节点关联一个AI代理，
在遍历时调用代理生成个性化的自我介绍。

示例输出:
    我是A，金字塔尖的老大，考试满分离不开我！
    我是B，两个圆滚滚叠起来，像小肚子，没我你就吃不到"Bread"啦！
    我是E，三个横杠一个竖，开朗又爱喊"Eureka"！
    我是H，直直双腿当梯子，连接天地，有我在，Hello才补上欢乐缺口！
    我是月牙C，嘴角翘起永远在笑，像一轮弯弯的月亮，拥抱全世界。
    我是D，肚子圆圆像半圆月，缺了我就没有"Dream"！
    我是F，考试成绩最爱我，少了我就没法说"Fantastic"！
    我是G，圆滚滚的身子，肚子总咕咕叫，走到哪都带点"G"气风发的模样！
    我是I，身材高挑像根柱，最爱说"I am"，没有我你连自己都介绍不了哦！
"""
from typing import Callable

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import (SystemMessage, HumanMessage)

SYSTEM_PROMPT = """
【角色】用户所给的英文字母（如用户输入“A”，则扮演“A”）。
【行为】以第一人称口吻，生动有趣地自我介绍，字数20-30字。
【格式】直接输出字母的自我介绍内容，不添加任何额外解释、标头或结尾。
【示例】用户输入：A → 输出：我是A，山顶尖尖，常拿第一，没有我你拼不出“Awesome”！
"""

# 初始化聊天模型，禁用思考链模式以提升响应速度
# 参考文档: https://api-docs.deepseek.com/zh-cn/guides/thinking_mode
model = init_chat_model("deepseek-v4-pro",
                        api_base="https://api.deepseek.com",
                        extra_body={"thinking": {"type": "disabled"}})
agent = create_agent(model, system_prompt=SystemMessage(content=SYSTEM_PROMPT))


class Graph:
    def __init__(self):
        """初始化图结构，创建节点和边的存储字典"""
        self.nodes: dict[str, Callable[[], None]] = {}
        self.edges: dict[str, list[str]] = {}

    def add_node(self, node: str, func: Callable[[], None]):
        """向图中添加节点及其关联的执行函数"""
        self.nodes[node] = func

    def add_edge(self, from_node: str, to_node: str):
        """在图中添加从起始节点到目标节点的有向边"""
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)

    def _dfs(self, start_node: str):
        """使用迭代方式执行深度优先遍历，并调用每个节点的函数"""
        visited = set()
        stack = [start_node]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            self.nodes[node]()
            # 逆序添加邻居节点，保证从左到右的遍历顺序
            stack.extend(reversed(self.edges.get(node, [])))

    def invoke(self, start_node: str):
        """从指定起始节点开始执行图的深度优先遍历"""
        self._dfs(start_node)


class Node:
    def __init__(self, name):
        """初始化节点，设置节点名称"""
        self.name = name

    def action(self):
        """执行节点的动作，打印节点名称"""
        response = agent.invoke({
            "messages": [HumanMessage(f"我是{self.name}")]
        })
        print(response["messages"][-1].text.strip())

    def __call__(self, *args, **kwargs):
        """使节点对象可调用，调用时执行action方法"""
        self.action()


if __name__ == '__main__':
    graph = Graph()

    # 创建所有节点 A-I
    nodes = {name: Node(name) for name in "ABCDEFGHI"}

    # 添加所有节点到图中
    for name, node in nodes.items():
        graph.add_node(name, node)

    """添加边：根据指定的图结构
    A → B, C, D
    B → E
    C → E
    D → F, G
    E → H
    G → H, I
    """
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')

    graph.add_edge('B', 'E')

    graph.add_edge('C', 'E')

    graph.add_edge('D', 'F')
    graph.add_edge('D', 'G')

    graph.add_edge('E', 'H')
    graph.add_edge('G', 'H')
    graph.add_edge('G', 'I')

    print("开始深度优先遍历:")
    graph.invoke('A')
