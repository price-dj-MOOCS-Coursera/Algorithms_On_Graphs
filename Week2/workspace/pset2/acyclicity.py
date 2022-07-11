#Uses python3

import sys


def acyclic(adj):
    visited = [False] * n
    exploredTwice = [0] * n

    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, visited, exploredTwice, v)
    print(exploredTwice)
    if max(exploredTwice) >= 1:
        return 1
    return 0


def explore(adj, visited, exploredTwice, v):

    visited[v] = True
    for w in adj[v]:
        print(w)
        if visited[w]:
            exploredTwice[w] += 1
            return

        explore(adj, visited, exploredTwice, w)
    #return exploredTwice


if __name__ == '__main__':
    file1 = open("04.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(adj)
    print(acyclic(adj))
