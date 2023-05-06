# Medium 1498. Number of Subsequences That Satisfy the Given Sum Condition
# You are given an array of integers nums and an integer target.
# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target.
# min(subseq) + max(subseq) <= target
# Since the answer may be too large, return it modulo 10^9 + 7.
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= nums[i] <= 10^6       !!! ВАЖНО !!!
#   1 <= target <= 10^6        !!! ВАЖНО !!!

class Solution:
    def numSubseq(self, nums, target):
        nums.sort()
        i = 0; j = len(nums)-1; sum = 0; mod = 10**9+7
        while i <= j:
            if nums[i] + nums[j] <= target:
                sum = (sum + 2**(j-i)) % mod
                i += 1
            else:
                j -= 1
        return sum

sln = Solution()
print(sln.numSubseq(nums=[3,5,6,7], target=9))

sln = Solution()
print(sln.numSubseq(nums=[3,3,6,8], target=10))

sln = Solution()
print(sln.numSubseq(nums=[2,3,3,4,6,7], target=12))