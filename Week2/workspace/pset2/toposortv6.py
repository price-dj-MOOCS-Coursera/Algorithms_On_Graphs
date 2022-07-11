#python3

import sys

# def dfs(adj, used, order, x):
#     stack = [len(adj)]
#
#     while stack:
#
#     pass


def toposort(adj):
    #used = [0] * len(adj)
    order = []
    visited = set()
    path = [object()]
    pathSet = set(path)
    stack = list(adj.keys())
    print(stack)

    while stack:
        for v in reversed(stack):
            if v not in visited:
                visited.add(v)
                path.append(v)
                pathSet.add(v)
                w = adj.get(v, [-1])
                print(w)
                stack.append(w)
        else:
            pathSet.remove(path.pop())
            order.append(v)
            stack.pop()
    print(visited)
    print(path)
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

