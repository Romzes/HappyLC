# Hard 839. Similar String Groups

class Solution:
    def numSimilarGroups(self, strs):
        size = len(strs)
        if size <= 1: return size
        uf = UnionFind(size)
        for i in range(1, size):
            for j in range(i):
                if self.is_similar(s1=strs[i], s2=strs[j]):
                    uf.union(i, j)
                    # print(i, strs[i], j, strs[j])
        return uf.groups

    def is_similar(self, s1, s2):
        diff = 0
        for i, c1 in enumerate(s1):
            if c1 == s2[i]: continue
            diff += 1
            if diff > 2: return False
        return True

class UnionFind:
    def __init__(self, size):
        # nodes: 0,1, ... size-1
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the 'rank' of each vertex.
        # The initial 'rank' of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.groups = size

    # The find function here is the same as that in the disjoint set with path compression.
    def find_root(self, x):
        if x == self.root[x]: return x
        # не просто находим корень, но и все элементы цепочки теперь ссылаются на корень
        self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find_root(x)
        rootY = self.find_root(y)
        if rootX == rootY: return
        self.groups -= 1
        if self.rank[rootX] > self.rank[rootY]: self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]: self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def normalize(self):
        for x in range(len(self.root)): self.find_root(x)

sln = Solution()
print(sln.numSimilarGroups(strs=['tars','rats','arts','star']))

sln = Solution()
print(sln.numSimilarGroups(strs=['omv','ovm']))

sln = Solution()
print(sln.numSimilarGroups(strs=['kccomwcgcs','socgcmcwkc','sgckwcmcoc','coswcmcgkc','cowkccmsgc','cosgmccwkc','sgmkwcccoc','coswmccgkc','kowcccmsgc','kgcomwcccs']))

sln = Solution()
print(sln.numSimilarGroups(strs=['ajdidocuyh','djdyaohuic','ddjyhuicoa','djdhaoyuic','ddjoiuycha','ddhoiuycja','ajdydocuih','ddjiouycha','ajdydohuic','ddjyouicha']))




