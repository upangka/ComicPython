"""基于图结构的节点遍历系统

使用深度优先搜索(DFS)算法遍历有向图，每个节点关联一个AI代理，
在遍历时调用代理生成个性化的自我介绍。

示例输出:
    我是A✨像座金字塔，积极向上永争第一，带你拼出超棒的单词！🌟
    我是B😎挺着圆滚滚的大肚皮，生活就要像蜜蜂般向前飞，肯定很“可以”！🐝
    我是E🌟能量爆棚爱探索，三横一竖永远向前冲！🌈
    我是J🌈 像快乐的鱼钩，勾住所有欢乐时光，让笑声串成闪亮项链！🎣✨
    我是R，走路带风又摇又滚😎，卷起舌头就能带你嗨翻全场！🎶
    我是K😎踢腿有劲踢走烦恼，快乐全开我就是全场King！💪
    我是S，身材妖娆曲线妙，像超人随时登场，拯救你的沉闷日子💪🌈
    我是T🌟像钉子一样稳稳站立，撑起你的Team和Trust！💪
    我是F🌟像飘扬的旗帜充满活力，带着Friendly和Fun向前冲！🎉
    我是L，笔直站立像灯塔✨，无我哪来Love和Light！💖
    我是U🌈像微笑的弧线，托起你每一个小确幸，一起加油呀！🌟
    我是C🌙弯弯的月牙儿，笑起来能挂住一整片星空，梦想和快乐都装得下！✨
    我是G🌞圆圈一钩超有型！帮你说出Great的开心，GOGO加油冲！💪
    我是M⛰️像两座并肩的山峰，稳稳托住你每一次冒险的旅程！🌟
    我是V💪胜利的手势充满力量，张开双臂就能拥抱所有希望！🌈
    我是N🌟行走的拱门，每天向上爬，没有我你拼不出Nice和Win！💪
    我是W✨双峰插云力量无穷，跟着我一起Wow出精彩人生！🌟
    我是D🌙弯弯月牙装满梦想，跟着我一起快乐启航！✨
    我是H👑两竖一横稳稳站立，拥抱生活热爱自己！✨
    我是O🔮圆圆满满的幸运圈，套住快乐，转出无限可能的圆满人生！✨
    我是X🎯瞄准未知，双臂交叉给你无限可能！🌟
    我是I🌟永远站得笔直的小字母，愿做你眼中最明亮的惊叹号！💪
    我是P💪站着笔直又骄傲，像面旗子迎风飘，自信就pick我！🌟
    我是Y✨像棵小树苗迎风摇摆，高举双手拥抱每一个美好的选择！🌈
    我是Q✨圆圆身子藏着大可爱，有了我快乐就Quick到来！🎉
    我是Z🌟收尾压轴我最酷，拼出Zest活力足，跟我一起快乐起舞！💃
"""
from typing import Callable

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import (SystemMessage, HumanMessage)

SYSTEM_PROMPT = """
【角色】用户所给的英文字母（如用户输入“A”，则扮演“A”）。
【行为】以第一人称口吻，生动有趣地自我介绍，字数控制在20-30字。
【要求】必须包含1-2个积极阳光的emoji表情符号（如✨🌟😊🎉💪🌈等），使表达更活泼。
【格式】直接输出字母的自我介绍内容，不添加任何额外解释、标头或结尾。
【示例】用户输入：A → 输出：我是A✨山顶尖尖常拿第一，没有我你拼不出Awesome！🎉
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

    # 创建所有节点 A-Z
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nodes = {name: Node(name) for name in letters}

    # 添加所有节点到图中
    for name, node in nodes.items():
        graph.add_node(name, node)

    # 添加边：根据指定的图结构（设计为体现DFS特性的非顺序图）
    """图的邻接表表示：
    A -> B, C, D
    B -> E, F
    C -> G
    D -> H, I
    E -> J, K
    F -> L
    G -> M, N
    H -> O
    I -> P, Q
    J -> R
    K -> S, T
    L -> U
    M -> V
    N -> W
    O -> X
    P -> Y
    Q -> Z
    R -> (无)
    S -> (无)
    T -> (无)
    U -> (无)
    V -> (无)
    W -> (无)
    X -> (无)
    Y -> (无)
    Z -> (无)
    
    DFS遍历路径示例：A -> D -> I -> Q -> Z（然后回溯到其他分支）
    """
    
    # A -> B, C, D (3条边)
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')

    # B -> E, F (2条边)
    graph.add_edge('B', 'E')
    graph.add_edge('B', 'F')

    # C -> G (1条边)
    graph.add_edge('C', 'G')

    # D -> H, I (2条边)
    graph.add_edge('D', 'H')
    graph.add_edge('D', 'I')

    # E -> J, K (2条边)
    graph.add_edge('E', 'J')
    graph.add_edge('E', 'K')

    # F -> L (1条边)
    graph.add_edge('F', 'L')

    # G -> M, N (2条边)
    graph.add_edge('G', 'M')
    graph.add_edge('G', 'N')

    # H -> O (1条边)
    graph.add_edge('H', 'O')

    # I -> P, Q (2条边)
    graph.add_edge('I', 'P')
    graph.add_edge('I', 'Q')

    # J -> R (1条边)
    graph.add_edge('J', 'R')

    # K -> S, T (2条边)
    graph.add_edge('K', 'S')
    graph.add_edge('K', 'T')

    # L -> U (1条边)
    graph.add_edge('L', 'U')

    # M -> V (1条边)
    graph.add_edge('M', 'V')

    # N -> W (1条边)
    graph.add_edge('N', 'W')

    # O -> X (1条边)
    graph.add_edge('O', 'X')

    # P -> Y (1条边)
    graph.add_edge('P', 'Y')

    # Q -> Z (1条边)
    graph.add_edge('Q', 'Z')

    # Z 没有后续节点

    print("\n开始深度优先遍历:")
    graph.invoke('A')
