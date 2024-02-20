"""
268 (Easy) Missing Number
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
Constraints:
  n == nums.length
  1 <= n <= 10^4
  0 <= nums[i] <= n
  All the numbers of nums are unique.
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

sln = Solution()
print(sln.missingNumber(nums=[3,0,1]))

sln = Solution()
print(sln.missingNumber(nums=[0,1]))

sln = Solution()
print(sln.missingNumber(nums=[9,6,4,2,3,5,7,0,1]))