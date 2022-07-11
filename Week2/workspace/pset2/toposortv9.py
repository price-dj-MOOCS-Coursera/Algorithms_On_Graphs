#Uses python3

import sys
from collections import deque

clock = 1

def dfs(adj, used, order, x):
    #write your code here
    used[x] = True
    for w in adj[x]:
        #print(w)
        #if not used[w]:
            print(w)
            dfs(adj, used, order, w)
    #a = postvisit(x)
    order.appendleft(x)
    #print(str(x) + " : " + str(a))
    #order[x] = a
    #order.append(x)
    #return

def postvisit(x):
    global clock
    result = clock
    clock += 1
    return result

def toposort(adj):
    used = [False] * len(adj)
    #order = queue.Queue(maxsize=len(adj))
    #order = []
    order = deque(maxlen=len(adj))

    for x in range(len(adj)):
        #print(x)
        if not used[x]:
            dfs(adj, used, order, x)

    print(order)
    #order = sorted(order, key=order.get, reverse=True)
    #orderList = list(order.values())
    order = list(order)
    return order

if __name__ == '__main__':
    file1 = open("01top.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]#dict([(i, []) for i in range(n)]) #
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(adj)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

