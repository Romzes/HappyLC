# 216 (Medium) Combination Sum III
"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.

Return a list of all possible valid combinations.
The list must not contain the same combination twice, and the combinations may be returned in any order.

Constraints:
  2 <= k <= 9
  1 <= n <= 60
"""

from typing import List

# есть рекурсия - проще код
# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.01 MB  Beats 16.14%
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res_list = []
        self.k = k
        self.comb = []  # 1 <= d_1 < ... < d_m <= 9
        self.backtrack(rest=n)
        return self.res_list

    def backtrack(self, rest):
        if len(self.comb) == self.k:
            if rest == 0: self.res_list.append(self.comb[::])  # добавляется очередная комбинация
            return
        start_d = 1 if len(self.comb) == 0 else (self.comb[-1] + 1)
        for d in range(start_d, 10):
            next_rest = rest - d
            if next_rest < 0: return
            self.comb.append(d)
            self.backtrack(rest=next_rest)
            self.comb.pop()


sln = Solution()
print(sln.combinationSum3(k=3, n=7))  # Output: [ [1,2,4] ]

sln = Solution()
print(sln.combinationSum3(k=3, n=9))  # Output: [ [1,2,6] , [1,3,5] , [2,3,4] ]

sln = Solution()
print(sln.combinationSum3(k=4, n=1))  # Output: []

