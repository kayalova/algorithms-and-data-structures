from collections import deque

def bfs(graph: dict, root) -> set:
    """
    :param graph: dict
    :param root: str or int
    :return: set of nodes
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
