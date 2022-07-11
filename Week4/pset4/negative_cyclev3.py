#Uses python3

import sys

class Stack(object):

   def __init__(self):
      self.items = []

   def push(self, item):
      self.items.append(item)

   def pop(self):
       return self.items.pop()

   def peek(self):
       return self.items[-1]

   def isEmpty(self):
       return len(self.items) == 0

cycleStack = Stack


def negative_cycle(adj, cost):
    marked = [False] * len(adj)
    onStack = [False] * len(adj)
    edgeTo = [None] * len(adj)

    for u in range(len(adj)):
        cycleBool = dfs(adj, u, marked, onStack, edgeTo)
    return 0

def dfs(adj, u, marked, onStack, edgeTo):
    onStack[u] = True
    marked[u] = True

    for v, w in zip(adj[u], cost[u]):

        if not cycleStack == None:
            return

        elif not marked[v]:
            edgeTo[v] = w
            dfs(adj, v, marked, onStack, edgeTo)

        elif onStack[]


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
