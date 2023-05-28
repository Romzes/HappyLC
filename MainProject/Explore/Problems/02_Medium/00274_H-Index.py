# Medium 274. H-Index
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia:
# The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

class Solution:
    def hIndex(self, citations):
        n = len(citations); h = -1
        citations.sort()
        for i, c in enumerate(citations):
            h1 = min(c, n-i)
            if h1 >= h: h = h1
            else: break
        return h

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i+1: return i
        return len(citations)

sln = Solution()
print(sln.hIndex(citations=[3,0,6,1,5]))

sln = Solution()
print(sln.hIndex(citations=[1,3,1]))

sln = Solution()
print(sln.hIndex(citations=[1,1,1,1,2,2,3]))

sln = Solution()
print(sln.hIndex(citations=[1]))
