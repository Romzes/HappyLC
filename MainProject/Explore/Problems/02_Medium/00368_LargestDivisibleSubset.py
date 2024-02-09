"""
368 (Medium) Largest Divisible Subset
Given a set of distinct positive integers nums,
return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
  answer[i] % answer[j] == 0, or
  answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.
Constraints:
  1 <= nums.length <= 1000
  1 <= nums[i] <= 2 * 10^9
  All the integers in nums are unique.
"""
from typing import List

# Runtime 209 ms , Beats 84.47% of users with Python3
# Memory 16.95 MB , Beats 65.23%of users with Python3
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1: return [nums[0]]
        nums.sort()
        dp = {nums[0]: [1, None]}  # [max_len, prev_val]
        max_len = 1; max_val = nums[0]
        for i in range(1, n):
            v = nums[i]
            dp[v] = [1, None]
            for j in range(i-1, -1, -1):
                u = nums[j]
                if v % u == 0 and dp[v][0] <= dp[u][0]:
                    dp[v][0], dp[v][1] = dp[u][0] + 1, u
            if dp[v][0] > max_len: max_len, max_val = dp[v][0], v
        res = []
        v = max_val
        while v is not None:
            res.append(v)
            v = dp[v][1]
        res.reverse()
        return res

# Runtime 96 ms , Beats 100.00% of users with Python3
# Memory 17.12 MB , Beats 57.46% of users with Python3
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1: return [nums[0]]
        nums.sort()
        dp = {nums[0]: [1, None]}  # [max_len, prev_val]
        max_len = 1; max_val = nums[0]
        for i in range(1, n):
            v = nums[i]
            dp[v] = [1, None]
            sqrt_v = int(v**0.5)
            if i <= 2*sqrt_v:
                for j in range(i-1, -1, -1):
                    u = nums[j]
                    if v % u == 0 and dp[v][0] <= dp[u][0]:
                        dp[v][0], dp[v][1] = dp[u][0] + 1, u
            else:
                for j in range(1, sqrt_v+1):
                    w, r = divmod(v, j)
                    if r != 0: continue
                    for u in (w, j):
                        if u in dp and dp[v][0] <= dp[u][0]:
                            dp[v][0], dp[v][1] = dp[u][0] + 1, u
            if dp[v][0] > max_len: max_len, max_val = dp[v][0], v
        res = []
        v = max_val
        while v is not None:
            res.append(v)
            v = dp[v][1]
        # res.reverse()
        return res

sln = Solution()
print(sln.largestDivisibleSubset(nums=[3,4,16,8]))

sln = Solution()
print(sln.largestDivisibleSubset(nums=[1,2,3]))

sln = Solution()
print(sln.largestDivisibleSubset(nums=[1,2,4,8]))


