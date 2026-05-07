def bfs(graph, start):
    """
    BFS广度优先搜索遍历图

    Args:
        graph: 邻接表表示的图 {节点: [邻居列表]}
        start: 起始节点

    Returns:
        list: BFS遍历顺序的节点列表

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
        >>> bfs(graph, 'A')
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    """
    queue = [start]
    visited = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited





if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
