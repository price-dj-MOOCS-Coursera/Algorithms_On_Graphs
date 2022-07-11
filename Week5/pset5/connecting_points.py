#Uses python3
import sys
import math
import heapq

class UnionFind:
    """Union-find data structure.

        Each unionFind instance X maintains a family of disjoint sets of
        hashable objects, supporting the following two methods:

        - find[item] returns a name for the set containing the given item.
          Each set is named by an arbitrarily-chosen one of its members; as
          long as the set remains unchanged it will keep the same name. If
          the item is not yet part of a set in X, a new singleton set is
          created for it.

        - X.union(item1, item2, ...) merges the sets containing each item
          into a single larger set.  If any item is not yet part of a set
          in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parent = {}

def minimum_distance(x, y):
    result = 0.
    heap = []
    heapq.heapify(heap)

    # build graph - edges from all xy
    # to every other xy

    for a, b in zip(x, y):
        for c, d in zip(x, y):
            if not (a == c and b == d):
                dist = math.sqrt(math.pow(a - c, 2) + math.pow(b - d, 2))
                heapq.heappush(heap, (dist, a, b))





    return result


if __name__ == '__main__':
    file1 = open("01con.txt", "r")
    input = file1.read()
    #input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print(x)
    print(y)
    print("{0:.9f}".format(minimum_distance(x, y)))
