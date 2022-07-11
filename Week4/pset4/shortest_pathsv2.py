# Uses python3

import sys
import queue

q = queue.Queue()

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here

    negative_cycle(adj, cost, distance, reachable, shortest, s)

    print(q.qsize())

    for s in range(q.qsize()):
        bfs(adj, cost, shortest, s)

    print(shortest)
    print(reachable)
    print(distance)

    return


def negative_cycle(adj, cost, distance, reachable, shortest, s):
    # prev = [None] * len(adj)
    shortest[s] = 0
    distance[s] = 0
    reachable[s] = True
    for u in range(len(adj) - 1):
        for v, w in zip(adj[u], cost[u]):
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                shortest[v] = distance[v]
                reachable[v] = True

    for v, w in zip(adj[s], cost[s]):
        if distance[v] > distance[s] + w:
            distance[v] = distance[s] + w
            shortest[v] = None
            reachable[v] = True
            q.put(v)




def bfs(adj, cost, shortest, s):
    q1 = queue.Queue()
    marked = [False] * len(adj)
    reachable[s] = True
    marked[s] = True
    #shortest[s] = 0
    q1.put(s)

    while not q1.empty():

        u = q1.get()
        print(u)
        for v, w in zip(adj[u], cost[u]):
            if not marked[v]:
                #shortest[v] = shortest[u] + w
                marked[v] = True
                #reachable[v] = True
                shortest[v] = None
                q1.put(v)




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
    distance = [float('inf')] * n
    reachable = [False] * n
    shortest = [None] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == False:
            print('*')
        elif shortest[x] == None:
            print('-')
        else:
            print(distance[x])
