"""
645 (Easy) Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n.
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
Constraints:
  2 <= nums.length <= 10^4
  1 <= nums[i] <= 10^4
"""

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [None, None]
        for i in range(len(nums)):
            while nums[i] > 0:
                j = nums[i]-1
                nums[i], nums[j] = nums[j], -nums[i]
            if i+1 != -nums[i]: res[0], res[1] = -nums[i], i+1
        return res

sln = Solution()
print(sln.findErrorNums(nums=[8,7,3,5,3,6,1,4]))

sln = Solution()
print(sln.findErrorNums(nums=[1,2,2,4]))

sln = Solution()
print(sln.findErrorNums(nums=[1,1]))