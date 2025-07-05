# 46 (Medium) Permutations
"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Constraints:
  1 <= nums.length <= 6
  -10 <= nums[i] <= 10
  All the integers of nums are unique.
"""

from typing import List

# есть рекурсия - проще код
# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.09 MB  Beats 33.27%
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        for i in range(len(self.nums)):
            if self.indexes[i]: continue
            self.indexes[i] = True
            self.comb.append(self.nums[i])
            self.backtracking()
            self.comb.pop()
            self.indexes[i] = False


sln = Solution()
res_list = sln.permute(nums=[1,2,3])
print(len(res_list), res_list)  # Output: [ [1,2,3] , [1,3,2] , [2,1,3] , [2,3,1] , [3,1,2] , [3,2,1] ]

sln = Solution()
res_list = sln.permute(nums=[0,1])
print(len(res_list), res_list)  # Output: [ [0,1] , [1,0] ]

sln = Solution()
res_list = sln.permute(nums=[1])
print(len(res_list), res_list)  # Output: [ [1] ]

sln = Solution()
res_list = sln.permute(nums=[1,2,3,4])
print(len(res_list), res_list)

sln = Solution()
res_list = sln.permute(nums=[1,2,3,4,5])
print(len(res_list), res_list)
