#Uses python3

import sys



def acyclic(adj):
    visited = [False] * n
    cc = 1
    ccNum = [cc] * n

    for v in range(len(adj)):
        path = []
        explore(adj, visited, ccNum, cc, path, v)
        cc += 1

        pathset = set(path)
        print(path)
        print(pathset)
        if len(pathset) != len(path):
            print(ccNum)
            return 1

    return 0


def explore(adj, visited, ccNum, cc, path, v):
    ccNum[v] = cc
    path.append(v)
    visited[v] = True

    for w in adj[v]:
        if w in path:
            path.append(w)
            return
        #path.append(w)
        #return
        explore(adj, visited, ccNum, cc, path, w)
        #path.append(w)



if __name__ == '__main__':
    file1 = open("07.txt", "r")
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
    #print(len(adj))
    print(acyclic(adj))
