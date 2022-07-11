#Uses python3

import sys

def dfs(adj, order, x):
    visited = set()
    stack = [x]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(adj[vertex] - visited)
    print(visited)
    return visited


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for x in adj:
        print(x)
        visited = dfs(adj, order, x)
    return visited

if __name__ == '__main__':
    file1 = open("01top.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = dict([(i, []) for i in range(n)]) #[[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(adj)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

