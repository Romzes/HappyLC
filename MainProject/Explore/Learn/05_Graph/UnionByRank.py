# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.vert = [i for i in range(size)]  # вершины для наглядности
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the 'rank' of each vertex.
        # The initial 'rank' of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY: return
        if self.rank[rootX] > self.rank[rootY]: self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]: self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(6)
uf.union(0, 1)
print(uf)
uf.union(2, 3)
print(uf)
uf.union(3, 4)
print(uf)
uf.union(0, 2)
print(uf)