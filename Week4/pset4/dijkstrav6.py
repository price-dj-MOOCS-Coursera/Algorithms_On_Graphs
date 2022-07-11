#Uses python3

import sys
from multiprocessing import Queue
import queue
import math
import heapq

class PriorityQueue(Queue):
    def _put(self, item):
        data, priority = item
        self._insort_right((priority,data))

    def _get(self):
        return self.queue.pop(0)

    def _insort_right(self, x):
        """Insert item x in list, and keep it sorted assuming a is sorted.
        If x is already in list, insert it to the right of the rightmost x.
        """
        a = self.queue
        lo = 0
        hi = len(a)

        while lo < hi:
            mid = (lo + hi) / 2
            if x[0] < a[mid][0]: hi = mid
            else: lo = mid + 1
        a.insert(lo, x)



def distance(adj, cost, s, t):
    #write your code here
    distTo = [math.inf] * len(adj)
    distTo[s] = 0
    prev = [None] * len(adj)

    pq = PriorityQueue()
    for i in range(len(distTo)):
        pq.put((i, distTo[i]))



    while not pq.empty():
        (distTo[u], u) = pq.get()
        #print(u)

        for w in cost[u]:
            #print(w)
            for v in adj[u]:
                if distTo[v] > distTo[u] + w:
                    distTo[v] = distTo[u] + w
                    prev[v] = u
                    #print(distTo[v])
                    pq.put((distTo[v], v))


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
