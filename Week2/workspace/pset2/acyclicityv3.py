#Uses python3

import sys



def acyclic(adj):
    visited = set()
    path = [object()]
    pathSet = set(path)
    stack = [iter(adj)]
    #print(stack)
    while stack:
        for v in stack[-1]:
            if v in pathSet:
                return 1
            elif v not in visited:
                visited.add(v)
                path.append(v)
                pathSet.add(v)
                stack.append(iter(adj.get(v, [])))
                break
        else:
            pathSet.remove(path.pop())
            stack.pop()
    return 0






if __name__ == '__main__':
    file1 = open("02.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = dict([(i, []) for i in range(n)]) #[[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #print(adj)
    #print(len(adj))
    print(acyclic(adj))
