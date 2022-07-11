#Uses python3

import sys

def dfs(adj, order, x):
    #write your code here
    #path = []
    stack = [x]
    label = len(adj)
    #order = {}
    while stack != []:
        v = stack.pop()
        if v not in order:
            order.append(v)
        for w in reversed(adj[v]):
            if w not in order and w not in stack:
                stack.append(w)
    #order = {v:k for k, v in order.items()}

    print(order)
    return order



def toposort(adj):
    used = [0] * len(adj)
    order = []
    orderList = []
    #maxLenOrder = 0
    for x in adj:
        order = dfs(adj, order, x)
        orderList.append(order)

    print(orderList)

    return order

if __name__ == '__main__':
    file1 = open("01top.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = dict([(i, []) for i in range(n)]) #[[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

