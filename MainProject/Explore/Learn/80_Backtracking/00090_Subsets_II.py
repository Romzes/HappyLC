# 90 (Medium) Subsets II
"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.

Constraints:
  1 <= nums.length <= 10
  -10 <= nums[i] <= 10
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.90 MB  Beats 84.81%
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.comb = []
        self.res_list = [[]]
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        for i in range(start_ind, len(self.nums)):
            if start_ind < i and self.nums[i-1] == self.nums[i]:
                continue
            self.comb.append(self.nums[i])
            self.res_list.append(self.comb[::])
            if i + 1 < len(self.nums): self.backtrack(start_ind=i + 1)
            self.comb.pop()


sln = Solution()
res_list = sln.subsetsWithDup(nums=[1,2,2])
print(len(res_list), res_list)  # Output: [ [] , [1] , [1,2] , [1,2,2] , [2] , [2,2] ]

sln = Solution()
res_list = sln.subsetsWithDup(nums=[0])
print(len(res_list), res_list)  # Output: [ [] , [0] ]