#Uses python3

import sys
from collections import deque


sys.setrecursionlimit(200000)

def dfs(adjRev, used, order, x):
    #write your code here
    used[x] = True
    for w in adjRev[x]:
        if not used[w]:
            dfs(adjRev, used, order, w)

    order.appendleft(x)

def toposort(adjRev):
    used = [False] * len(adjRev)
    order = deque(maxlen=len(adjRev))
    post = [0] * len(adjRev)
    for x in range(len(adjRev)):
        if not used[x]:
            dfs(adjRev, used, order, x)
    order = list(order)
    return order

def explore(adj, visited, scc, count, v):
    scc[v] = count
    visited[v] = True
    for w in adj[v]:
        #print(w)
        if not visited[w]:
            explore(adj, visited, scc, count, w)



def number_of_strongly_connected_components(adj, adjRev):
    count = 1
    visited = [False] * len(adjRev)
    scc = [0] * len(adjRev)
    postorder= toposort(adjRev)

    for v in postorder:
        #print(v)
        if not visited[v]:
            explore(adj, visited, scc, count, v)
            count += 1

    #print(scc)
    result = max(scc)
    return result

if __name__ == '__main__':
    #file1 = open("01scc.txt", "r")
    #input = file1.read()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adjRev = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    for (a, b) in edges:
        adjRev[b - 1].append(a - 1)
    #print(adj)
    #print(adjRev)
    print(number_of_strongly_connected_components(adj, adjRev))
