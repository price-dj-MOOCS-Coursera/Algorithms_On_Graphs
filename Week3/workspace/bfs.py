#Uses python3

import sys
import queue
import math

def distance(adj, s, t):
    #write your code here
    marked = [False] * len(adj)
    distTo = [None] * len(adj)

    distTo[s] = 0
    q = queue.Queue(maxsize=len(adj))

    q.put(s)
    marked[s] = True

    while not q.empty():
        v = q.get()
        for w in adj[v]:
            if not marked[w]:
                distTo[w] = distTo[v] + 1
                marked[w] = True
                q.put(w)

    if distTo[t] == None:
        return -1

    return distTo[t]

if __name__ == '__main__':
    #file1 = open("02bfs.txt", "r")
    #input = file1.read()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
