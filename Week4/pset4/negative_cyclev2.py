#Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [float('inf')] * len(adj)
    prev = [0] * len(adj)
    x = 0
    visited = [False] * len(adj)

    for s in range(len(adj)):
        if not visited[s]:
            visited[s] = True
            dist[s] = 0
            for i in range(len(adj) - 1):
                for u in range(len(adj)):
                    visited[u] == True
                    #if not u == s:
                    #if not visited[u]:
                    for v, w in zip(adj[u], cost[u]):
                            #if not visited[v]:
                            if dist[v] > dist[u] + w:
                                dist[v] = dist[u] + w
                                prev[v] = u

            distCopy = dist[:]
            # run Bellman-Ford Vth time

            for v, w in zip(adj[u], cost[u]):
                #if not visited[v]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    return 1

            # for i in range(len(dist)):
            #      if not dist[i] == distCopy[i]:
            # #         # is negative cycle
            # #         #x = prev[i]
            #          return 1







    return 0


if __name__ == '__main__':
    file1 = open("03neg.txt", "r")
    input = file1.read()

    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
