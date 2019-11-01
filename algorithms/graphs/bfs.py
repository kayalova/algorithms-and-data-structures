from collections import deque

def bfs(graph: dict, root) -> set:
    """
    :param graph: dict
    :param root: str or int; represent root node
    :return: list of nodes
    """
    queue = deque()
    queue.extend(graph[root])
    visited = set([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            queue.extend(graph[node])
            visited.add(node)

    return visited


graph = {
    'a': set(['b', 'c']),
    'b': set(['a', 'e']),
    'c': set(['a', 'd']),
    'e': set(['b']),
    'd': set(['c', 'f', 'g', 'h']),
    'h': set(['d']),
    'f': set(['d']),
    'g': set(['d']),
}

graph2 = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

