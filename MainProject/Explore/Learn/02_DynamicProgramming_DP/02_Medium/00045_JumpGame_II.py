# 45 (Medium) Jump Game II
"""
You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
  0 <= j <= nums[i] and
  i + j < n

Return the minimum number of jumps to reach nums[n-1].
The test cases are generated such that you can reach nums[n - 1].

Constraints:
  1 <= nums.length <= 10^4
  0 <= nums[i] <= 1000
  It's guaranteed that you can reach nums[n-1].
"""

from typing import List

# !!! ОЧЕНЬ МЕДЛЕННО !!!
# Runtime = 1357ms  Beats 21.93%  ;  Memory = 18.52MB  Beats 75.24%
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        dp = n * [float('+inf')]  # n >= 2
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            if i + nums[i] >= n-1:
                dp[i] = 1
                continue
            dp[i] = 1 + min(dp[i+j] for j in range(nums[i]+1))
        return dp[0]


sln = Solution()
print(sln.jump(nums=[2,3,1,1,4]))  # Output: 2
""" Explanation
The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

sln = Solution()
print(sln.jump(nums = [2,3,0,1,4]))  # Output: 2

"""
0 100_439 10.04 9.59
1 478_263 47.83 45.65
2 246_677 24.67 23.55
3-4 130_625 13.06 12.47
5-6 30_704 3.07 2.93
7-9 21_857 2.19 2.09
10 и более 39_031 3.90 3.73
"""

a = 4.7
b = round(a)
print(type(b), b)

# 1 047 596 м2 104.76 га 46.94 %
print(100_439 + 478_263 + 246_677 + 130_625 + 30_704 + 21_857 + 39_031)  # 1_047_596 м2
print(10.04 + 47.83 + 24.67 + 13.06 + 3.07 + 2.19 + 3.90)  # 104.76 га
print(9.59 + 45.64 + 23.55 + 12.47 + 2.93 + 2.09 + 3.73)  # 100.00 %
