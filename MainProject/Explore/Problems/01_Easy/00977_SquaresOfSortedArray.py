"""
977 (Easy) Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order
return an array of the squares of each number sorted in non-decreasing order.
"""
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lng = len(nums); res = lng * [0]
        for i in range(lng): nums[i] = nums[i] * nums[i]
        i, j = 0, lng-1
        for k in range(lng-1, -1, -1):
            if nums[i] >= nums[j]:
                res[k] = nums[i]; i += 1
            else:
                res[k] = nums[j]; j -= 1
        return res

sln = Solution()
print(sln.sortedSquares(nums=[-4,-1,0,3,10]))

sln = Solution()
print(sln.sortedSquares(nums=[-7,-3,2,3,11]))