#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    used[x] = True
    for w in adj[x]:
        if not used[w]:
            dfs(adj, used, order, w)
    return v


def toposort(adj):
    used = [False] * len(adj) #[0] * len(adj)
    order = []
    for x in adj:
        w = dfs(adj, used, order, x)
        order.append(w)
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
    print(adj)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

