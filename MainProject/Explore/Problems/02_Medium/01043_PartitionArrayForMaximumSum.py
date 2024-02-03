"""
1043 (Medium) Partition Array for Maximum Sum
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k.
After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning.
Test cases are generated so that the answer fits in a 32-bit integer.
Constraints:
  1 <= arr.length <= 500
  0 <= arr[i] <= 10^9
  1 <= k <= arr.length
"""
from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr); dp = n * [0]; a = 0
        for i in range(k):
            a = max(a, arr[i])
            dp[i] = (i+1)*a
        for i in range(k, n):
            a = 0
            for j in range(k):
                a = max(a, arr[i-j])
                dp[i] = max(dp[i], dp[i-j-1] + (j+1)*a)
        return dp[-1]

sln = Solution()
print(sln.maxSumAfterPartitioning(arr=[1,15,7,9,2,5,10], k=3))

sln = Solution()
print(sln.maxSumAfterPartitioning(arr=[1,4,1,5,7,3,6,1,9,9,3], k=4))

sln = Solution()
print(sln.maxSumAfterPartitioning(arr=[1], k=1))