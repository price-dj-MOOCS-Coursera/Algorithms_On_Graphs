#Uses python3

import sys
import queue
import math

from queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        #self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, item))
        #self.counter += 1

    def get(self, *args):
        _, item = PriorityQueue.get(self, *args)
        return item

def distance(adj, cost, s, t):
    #write your code here
    distTo = [math.inf] * len(adj)
    distTo[s] = 0
    prev = [None] * len(adj)

    pq = MyPriorityQueue()
    for i in range(len(distTo)):
        pq.put(i, distTo[i])

    while not pq.empty():
        u = pq.get()
        print(u)

        for w in cost[u]:
            #print(w)
            for v in adj[u]:
                if distTo[v] > distTo[u] + w:
                    distTo[v] = distTo[u] + w
                    prev[v] = u
                    #print(distTo[v])
                    pq.put(v, distTo[v])


    if distTo[t] == math.inf:
        return -1
    print(distTo)
    print(prev)
    return distTo[t]


if __name__ == '__main__':
    file1 = open("01dijk.txt", "r")
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
    s, t = data[0] - 1, data[1] - 1
    print(adj)
    print(cost)
    print(distance(adj, cost, s, t))
