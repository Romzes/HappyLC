# Hard 1770. Maximum Score from Performing Multiplication Operations
# You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.
# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:
#   Choose one integer x from either the start or the end of the array nums.
#   Add multipliers[i] * x to your score.
#       Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
#   Remove x from nums.
# Return the maximum score after performing m operations.

class Solution:
    def maximumScore(self, nums, multipliers):
        pass

sln = Solution()
print(sln.maximumScore(nums=[1,2,3], multipliers=[3,2,1]))

sln = Solution()
print(sln.maximumScore(nums=[-5,-3,-3,-2,7,1], multipliers=[-10,-5,3,4,6]))