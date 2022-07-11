#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here

    negCycle = negative_cycle(adj, cost, distance, reachable, shortest, s)

    return



def negative_cycle(adj, cost, distance, reachable, shortest, s):
    #prev = [None] * len(adj)
    distance[s] = 0
    reachable[s] = 0
    for u in range(len(adj) - 1):
            for v, w in zip(adj[u], cost[u]):

                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    reachable[v] = u
                    #shortest[v] = distance[v]

    for v, w in zip(adj[s], cost[s]):
            if distance[v] > distance[s] + w:
                distance[v] = distance[s] + w
                reachable[v] = s
                shortest[v] = 0
                return True

    return False


if __name__ == '__main__':
    file1 = open("01short.txt", "r")
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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [None] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == None:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

