# 3437 (Medium) Permutations III
"""
Given an integer n, an alternating permutation is a permutation of the first n positive integers such that no two adjacent elements are both odd or both even.
Return all such alternating permutations sorted in lexicographical order.

Constraints:
  1 <= n <= 10
"""

from typing import List

# есть рекурсия
# Runtime = 49 ms  Beats 88.89%  ;  Memory = 23.99 MB  Beats 80.25%
class Solution:
    def permute(self, n: int) -> List[List[int]]:
        self.n = n
        self.indexes = (n+1) * [False]
        self.comb = []
        self.res_list = []
        self.backtrack()
        return self.res_list

    def backtrack(self):
        # len(self.comb) <= n
        if len(self.comb) == self.n:
            self.res_list.append(self.comb[::])
            return
        # len(self.comb) <= n-1
        rng = range(1, self.n+1) if len(self.comb) == 0 else range(1 + self.comb[-1] % 2, self.n+1, 2)
        for i in rng:
            if self.indexes[i]: continue  # i in self.comb
            self.indexes[i] = True
            self.comb.append(i)
            self.backtrack()
            self.indexes[i] = False
            self.comb.pop()


sln = Solution()
res_list = sln.permute(n=4)
print(len(res_list), res_list)
# Output: [ [1,2,3,4] , [1,4,3,2] , [2,1,4,3] , [2,3,4,1] , [3,2,1,4] , [3,4,1,2] , [4,1,2,3] , [4,3,2,1] ]

sln = Solution()
res_list = sln.permute(n=2)
print(len(res_list), res_list)
# Output: [ [1,2] , [2,1] ]

sln = Solution()
res_list = sln.permute(n=3)
print(len(res_list), res_list)
# Output: [ [1,2,3] , [3,2,1] ]
