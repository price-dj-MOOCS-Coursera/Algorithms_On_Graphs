# Uses python3

import sys

def reach(adj, x, y):
    # write your code here
    # print(adj)
    visited = [False] * n
    visited = explore(adj, visited, x)
    if visited[y]:
        return 1
    return 0

def explore(adj, visited, v):
    # global visited
    visited[v] = True
    for w in adj[v]:
            if not visited[w]:
                explore(adj, visited, w)
    return visited


if __name__ == '__main__':
    #file1 = open("02.txt", "r")
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]  # dict([(i, []) for i in range(n)])
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


