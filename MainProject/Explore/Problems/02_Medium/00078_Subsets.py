# 78 (Medium) Subsets
"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.

Constraints:
  1 <= nums.length <= 10
  -10 <= nums[i] <= 10
  All the numbers of nums are unique.
"""

from typing import List

# есть рекурсия - проще код, есть оптимизации, уменьшается кол-во рекурсивных вызовов
# Runtime = 0ms  Beats 100.00%  ;  Memory = 17.94 MB  Beats 40.18%
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.comb = []
        self.res_list = [[]]
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        for i in range(start_ind, len(self.nums)):
            self.comb.append(self.nums[i])
            self.res_list.append(self.comb[::])
            if i+1 < len(self.nums): self.backtrack(start_ind=i+1)
            self.comb.pop()


sln = Solution()
subs = sln.subsets(nums=[1,2,3])
print(len(subs), subs)
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

sln = Solution()
subs = sln.subsets(nums=[0])
print(len(subs), subs)
# Output: [[],[0]]