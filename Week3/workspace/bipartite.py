#Uses python3

import sys
import queue

white = False
black = True
biPartate = True

def bipartite(adj):
    #write your code here
    #isBipartite = True

    colour = [None] * len(adj)
    marked = [False] * len(adj)

    for v in range(len(adj)):
        if not marked[v]:
            bfs(adj, colour, marked, v)
    if biPartate:
        return 1
    return 0

def bfs(adj, colour, marked, v):
    global white, black, biPartate

    q = queue.Queue(maxsize=len(adj))
    colour[v] = white
    marked[v] = True
    q.put(v)

    while not q.empty():
        v = q.get()
        for w in adj[v]:
            if not marked[w]:
                marked[w] = True
                colour[w] = not colour[v]
                q.put(w)
            elif colour[w] == colour[v]:
                biPartate = False



if __name__ == '__main__':
    #file1 = open("01bi.txt", "r")
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
    print(bipartite(adj))
