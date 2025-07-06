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
        self.comb = []  # [nums[i_1], nums[i2], ... nums[i_k]]
        # где 0 <= i_1 < i_2 < ... < i_k < len(nums) чтобы все подмножества были уникальными
        self.res_list = [[]]  # сразу добавили пустое множество
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        # start_ind = index of nums
        for i in range(start_ind, len(self.nums)):
            self.comb.append(self.nums[i])
            self.res_list.append(self.comb[::])
            if i+1 < len(self.nums): self.backtrack(start_ind=i+1)
            self.comb.pop()


# есть рекурсия
# Runtime = 0ms  Beats 100.00%  ;  Memory = 17.72MB  Beats 90.62%
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.indexes = []  # = [0 <= i_1 < i_2 < ... < i_k < len(nums)] чтобы все подмножества были уникальными
        self.comb = []     # = [nums[i_1], nums[i2], ... nums[i_k]]
        self.res_list = [[]]  # сразу добавили пустое множество
        self.backtrack()
        return self.res_list

    def backtrack(self):
        start_ind = 0 if not self.indexes else self.indexes[-1]+1
        for i in range(start_ind, len(self.nums)):
            self.indexes.append(i)
            self.comb.append(self.nums[i])
            self.res_list.append(self.comb[::])
            if i+1 < len(self.nums): self.backtrack()
            self.indexes.pop()
            self.comb.pop()


sln = Solution()
subs = sln.subsets(nums=[1,2,3])
print(len(subs), subs)
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

sln = Solution()
subs = sln.subsets(nums=[0])
print(len(subs), subs)
# Output: [[],[0]]