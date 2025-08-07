from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pass

sln = Solution()  # Example 1
sln.maxSubArrayLen(nums=[1,-1,5,-2,3], k=3)  # Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

sln = Solution()  # Example 2
sln.maxSubArrayLen(nums=[-2,-1,2,1], k=1)  # Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
