# 77 (Medium) Combinations
"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Constraints:
  1 <= n <= 20
  1 <= k <= n
"""

from typing import List

# рекурсия, оптимизация
# Runtime = 125ms  Beats 83.19%  ;  Memory = 59.45MB  Beats 94.85%
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n, self.k = n, k
        self.comb = []
        self.res_list = []
        self.backtrack()
        return self.res_list

    def backtrack(self):
        if len(self.comb) == self.k:
            self.res_list.append(self.comb[::])
            return

        start = 1 if not self.comb else self.comb[-1]+1
        if self.n - start + 1 < self.k - len(self.comb): return  # оптимизация

        for i in range(start, self.n+1):
            self.comb.append(i)
            self.backtrack()
            self.comb.pop()


sln = Solution()
res_list = sln.combine(n=4, k=2)  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(len(res_list), res_list)
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

sln = Solution()
res_list = sln.combine(n=1, k=1)  # Output: [[1]]
print(len(res_list), res_list)

sln = Solution()
res_list = sln.combine(n=5, k=3)
print(len(res_list), res_list)
