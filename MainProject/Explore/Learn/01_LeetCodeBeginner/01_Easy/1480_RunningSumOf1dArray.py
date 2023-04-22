# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)): nums[i] += nums[i-1]
        return nums

sln = Solution()
print(sln.runningSum(nums=[1,2,3,4]))

sln = Solution()
print(sln.runningSum(nums=[1,1,1,1,1]))

sln = Solution()
print(sln.runningSum(nums=[3,1,2,10,1]))