from collections import deque


def dfs_recursive(graph: dict, node, visited=[], visited_set=set()):
    """
    Depth-First Search
    :param graph: dict
    :param node: str or int
    :param visited: list of visited nodes; needed for saving visited nodes order
    :param visited_set: set of visited nodes
    :return: list of visited nodes
    """
    if node not in visited_set:
        visited.append(node)
        visited_set.add(node)
        for n in graph[node]:
            dfs_recursive(graph, n, visited, visited_set)
    return visited


def dfs_iterative(graph: dict, root):
    deq, visited, visited_set = deque(), [], set()
    deq.extend(graph[root])
    visited.append(root)
    visited_set.add(root)

    while deq:
        node = deq.popleft()
        if node not in visited_set:
            deq.extendleft(graph[node][::-1])
            visited.append(node)
            visited_set.add(node)

    return visited
