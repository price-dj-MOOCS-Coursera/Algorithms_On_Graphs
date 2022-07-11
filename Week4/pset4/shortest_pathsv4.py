# Uses python3

import sys
import queue



def shortet_paths(adj, cost, s, distance, reachable, shortest):
    shortest[s] = 0
    distance[s] = 0
    reachable[s] = True
    #prev = [None] * len(adj)
    #prev[s] = s
    arr = []

    for i in range(len(adj) - 1):
        for u in range(len(adj)):
            for v, w in zip(adj[u], cost[u]):

                #print("V-1 cycle v " + str(v))
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    shortest[v] = distance[v]
                    reachable[v] = True
                    #prev[v] = u

    for u in range(len(adj)):
        for v, w in zip(adj[u], cost[u]):

            #print("V cycle v " + str(v))
            if distance[v] > distance[u] + w:


                #distance[v] = distance[u] + w
                shortest[v] = None
                #reachable[v] = True
                arr.append(v)
                #print(arr)


    #print(arr)
    for s in arr:
        bfs(adj, shortest, s)

    #print(shortest)
    #print(reachable)
    #print(distance)
    #print(prev)

    return



def bfs(adj, shortest, s):
    q = queue.Queue()
    marked = [False] * len(adj)
    marked[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if not marked[v]:
                marked[v] = True
                #print("here")
                shortest[v] = None
                q.put(v)




if __name__ == '__main__':
    file1 = open("03short.txt", "r")
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
    #print(adj)
    #print(cost)
    shortet_paths(adj, cost, s, distance, reachable, shortest)

    for x in range(n):
        if reachable[x] == False:
            print('*')
        elif shortest[x] == None:
            print('-')
        else:
            print(distance[x])
