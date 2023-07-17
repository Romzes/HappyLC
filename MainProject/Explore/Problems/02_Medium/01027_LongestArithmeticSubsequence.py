# Medium 1027. Longest Arithmetic Subsequence
# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
# Note that:
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
# Constraints:
#   2 <= nums.length <= 1000
#   0 <= nums[i] <= 500

class Solution:
    def longestArithSeqLength(self, nums):
        N = len(nums)
        if N <= 2: return N
        

sln = Solution()
print(sln.longestArithSeqLength(nums=[3,6,9,12]))

sln = Solution()
print(sln.longestArithSeqLength(nums=[9,4,7,2,10]))

sln = Solution()
print(sln.longestArithSeqLength(nums=[20,1,15,3,10,5,8]))