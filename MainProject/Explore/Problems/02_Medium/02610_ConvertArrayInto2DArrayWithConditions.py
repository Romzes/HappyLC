"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.
Note that the 2D array can have a different number of elements on each row.

Constraints:
  1 <= nums.length <= 200
  1 <= nums[i] <= nums.length
"""

class Solution:
    def findMatrix(self, nums):
        nums.sort(); res = []; j = 0
        for i, n in enumerate(nums):
            if i == 0 or n != nums[i-1]: j = 0
            else: j += 1
            if j == len(res): res.append([])
            res[j].append(n)
        return res

sln = Solution()
print(sln.findMatrix(nums=[1,3,4,1,2,3,1]))

sln = Solution()
print(sln.findMatrix(nums=[1,2,3,4]))