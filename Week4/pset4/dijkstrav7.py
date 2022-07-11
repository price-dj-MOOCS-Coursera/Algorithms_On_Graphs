#Uses python3

import sys
#import queue
import math
import heapq
#from numpy import inf





def distance(adj, cost, s, t):

    dist = [float('inf')] * len(adj)
    dist[s] = 0
    #prev = [0] * len(adj)

    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (dist[s], s))

    while heap:
        _, u = heapq.heappop(heap)
        for v, w in zip(adj[u], cost[u]):
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                #prev[v] = u
                #print(v, w)
                heapq.heappush(heap, (dist[v], v))


    if dist[t] == float('inf'):
        return -1
    return dist[t]

if __name__ == '__main__':
    #file1 = open("03dijk.txt", "r")
    #input = file1.read()
    input = sys.stdin.read()
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
    s, t = data[0] - 1, data[1] - 1
    #print(adj)
    #print(cost)
    print(distance(adj, cost, s, t))
