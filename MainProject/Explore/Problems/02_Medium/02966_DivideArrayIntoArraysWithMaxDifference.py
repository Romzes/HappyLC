"""
You are given an integer array nums of size n and a positive integer k.
Divide the array into one or more arrays of size 3 satisfying the following conditions:
  Each element of nums should be in exactly one array.
  The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays.
If it is impossible to satisfy the conditions, return an empty array.
And if there are multiple answers, return any of them.
Constraints:
  n == nums.length
  1 <= n <= 10^5
  n is a multiple of 3.
  1 <= nums[i] <= 10^5
  1 <= k <= 10^5
"""
from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort(); res = []
        for i in range(0, len(nums), 3):
            arr = nums[i:i+3]
            if arr[-1] - arr[0] > k: return []
            res.append(arr)
        return res

sln = Solution()
print(sln.divideArray(nums=[1,3,4,8,7,9,3,5,1], k=2))

sln = Solution()
print(sln.divideArray(nums=[1,3,3,2,7,3], k=3))