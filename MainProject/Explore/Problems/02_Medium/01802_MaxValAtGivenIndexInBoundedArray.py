# Medium 1802. Maximum Value at a Given Index in a Bounded Array
# You are given three positive integers: n, index, and maxSum.
# You want to construct an array nums (0-indexed) that satisfies the following conditions:
#   nums.length == n
#   nums[i] is a positive integer where 0 <= i < n.
#   abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
#   The sum of all the elements of nums does not exceed maxSum.
#   nums[index] is maximized.
# Return nums[index] of the constructed array.
# Note that abs(x) equals x if x >= 0, and -x otherwise.
# Constraints:
#   1 <= n <= maxSum <= 10^9
#   0 <= index < n

class Solution:
    def maxValue(self, n, index, maxSum):
        pass

sln = Solution()
print(sln.maxValue(n=4, index=2, maxSum=6))

sln = Solution()
print(sln.maxValue(n=6, index=1, maxSum=10))