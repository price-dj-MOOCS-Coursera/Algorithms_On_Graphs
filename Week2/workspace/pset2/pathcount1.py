#Uses python3

import sys
from collections import deque

def reach(adj, x, y):
    # write your code here
    # print(adj)
    visited = [False] * len(adj)
    visited = explore(adj, visited, x)
    if visited[y]:
        return 1
    return 0

def explore(adj, visited, v):
    # global visited
    #print(visited)
    visited[v] = True
    for w in adj[v]:
            if not visited[w]:
                explore(adj, visited, w)
    return visited


def dfs(adj, used, order, x):
    #write your code here
    used[x] = True
    for w in adj[x]:
        if not used[w]:
            dfs(adj, used, order, w)
    order.appendleft(x)

def toposort(adj):
    used = [False] * len(adj)
    order = deque(maxlen=len(adj))

    for x in range(len(adj)):
        if not used[x]:
            dfs(adj, used, order, x)

    order = list(order)
    return order

def pathcount(adj, s, t):
    count = [0] * len(adj)
    order = toposort(adj)

    for v in range(len(adj)):

        for w in adj[v]:
            #c1 = reach(adj, s, w)
            #c2 = reach(adj, w, t)

            count[v] = c1 + c2
    return count

if __name__ == '__main__':
    file1 = open("05top.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]#dict([(i, []) for i in range(n)]) #
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #print(adj)
    order = toposort(adj)
    count = pathcount(adj, order[0], order[-1])
    for x in order:
        print(x + 1, end=' ')
    print()
    for x in count:
        print(x + 1, end=' ')

