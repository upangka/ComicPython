# 访问过的顶点
vertex = []


def dfs(graph, node):
    node not in vertex and vertex.append(node)
    for next_node in graph[node]:
        if next_node not in vertex:
            dfs(graph, next_node)




if __name__ == '__main__':
    """定义有向图的邻接表的形式，其中key为所有节点，value为该节点的邻接点列表
    value都是从A -> Xxx节点的值，也就说Xxx等节点
    """

    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['E'],
        'D': ['F', 'G'],
        'E': ['H'],
        'F': [],
        'G': ['H', 'I'],
        'H': [],
        'I': []
    }

    dfs(graph, 'A')
    # ['A', 'B', 'E', 'H', 'C', 'D', 'F', 'G', 'I']
    print(vertex)
