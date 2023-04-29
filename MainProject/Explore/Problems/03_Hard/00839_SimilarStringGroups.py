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
        uf.normalize()
        return len(set(uf.root))

    def is_similar(self, s1, s2):
        diff = 0
        for i, c1 in enumerate(s1):
            if c1 == s2[i]: continue
            diff += 1
            if diff > 2: return False
        return True

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find_root(self, x):
        if x == self.root[x]: return x
        self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find_root(x)
        rootY = self.find_root(y)
        if rootX == rootY: return
        if self.rank[rootX] > self.rank[rootY]: self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]: self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def normalize(self):
        for x in range(len(self.root)): self.find_root(x)

# sln = Solution()
# print(sln.numSimilarGroups(strs=['tars','rats','arts','star']))
#
# sln = Solution()
# print(sln.numSimilarGroups(strs=['omv','ovm']))
#
# sln = Solution()
# print(sln.numSimilarGroups(strs=['kccomwcgcs','socgcmcwkc','sgckwcmcoc','coswcmcgkc','cowkccmsgc','cosgmccwkc','sgmkwcccoc','coswmccgkc','kowcccmsgc','kgcomwcccs']))

sln = Solution()
print(sln.numSimilarGroups(strs=['ajdidocuyh','djdyaohuic','ddjyhuicoa','djdhaoyuic','ddjoiuycha','ddhoiuycja','ajdydocuih','ddjiouycha','ajdydohuic','ddjyouicha']))




