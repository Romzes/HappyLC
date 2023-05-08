# Easy 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):
        nums.sort()
        i = 0; j = len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s == target: return [i, j]
            if s < target: i += 1
            else: j -= 1

sln = Solution()
print(sln.twoSum(nums=[2,7,11,15], target=9))

sln = Solution()
print(sln.twoSum(nums=[3,2,4], target=6))

sln = Solution()
print(sln.twoSum(nums=[3,3], target=6))