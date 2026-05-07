"""
DFS深度优先搜索 - 迭代实现（使用栈）
时间复杂度：O(V + E)
空间复杂度：O(V)
适用场景：图的遍历、路径查找、连通分量检测
"""


def dfs_stack(graph, node):
    """
    使用栈实现DFS迭代遍历

    Args:
        graph: 邻接表表示的图 {节点: [邻居列表]}
        node: 起始节点

    Returns:
        list: DFS遍历顺序的节点列表

    Examples:
        >>> graph = {
        ...     'A': ['B', 'C', 'D'],
        ...     'B': ['E'],
        ...     'C': ['E'],
        ...     'D': ['F', 'G'],
        ...     'E': ['H'],
        ...     'F': [],
        ...     'G': ['H', 'I'],
        ...     'H': [],
        ...     'I': []
        ... }
        >>> dfs_stack(graph, 'A')
        ['A', 'B', 'E', 'H', 'C', 'D', 'F', 'G', 'I']
    """
    visited = []
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited





if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
