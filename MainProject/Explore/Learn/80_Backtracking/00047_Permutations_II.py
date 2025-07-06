# 47 (Medium) Permutations II
"""
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Constraints:
  1 <= nums.length <= 8
  -10 <= nums[i] <= 10
"""

from typing import List

# Runtime= 0 ms  Beats 100.00%  ;  Memory = 18.03 MB  Beats 53.31%
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.indexes = len(nums) * [False]
        self.comb = []
        self.res_list = []
        self.backtracking()
        return self.res_list

    def backtracking(self):
        if len(self.comb) == len(self.nums):
            self.res_list.append(self.comb[::])
            return
        vals = set()
        for i in range(len(self.nums)):
            v = self.nums[i]
            if self.indexes[i] or v in vals: continue
            vals.add(v)
            self.indexes[i] = True
            self.comb.append(v)
            self.backtracking()
            self.comb.pop()
            self.indexes[i] = False


sln = Solution()
res_list = sln.permuteUnique(nums=[1,1,2])
print(len(res_list), res_list)  # Output: [ [1,1,2] , [1,2,1] , [2,1,1] ]

sln = Solution()
res_list = sln.permuteUnique(nums=[1,2,3])
print(len(res_list), res_list)  # Output: [ [1,2,3] , [1,3,2] , [2,1,3] , [2,3,1] , [3,1,2] , [3,2,1] ]

sln = Solution()
res_list = sln.permuteUnique(nums=[1,1,1,1])
print(len(res_list), res_list)

sln = Solution()
res_list = sln.permuteUnique(nums=[1,1,1,1,2,2,2])
print(len(res_list), res_list)
