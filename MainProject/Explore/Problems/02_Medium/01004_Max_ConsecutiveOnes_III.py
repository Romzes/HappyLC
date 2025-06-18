# 1004 (Medium) Max Consecutive Ones III
"""
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1.
  0 <= k <= nums.length
"""

from typing import List
from collections import deque

# Runtime = 84 ms  Beats 11.78%  ;  Memory = 18.09 MB  Beats 99.58%
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        prev = deque([0], maxlen=k+1)  # 1 <= len(prev) <= k+1
        total = 0
        for a in nums:
            # nums = (0)(0)(1,0)(1,0)(1,1,1)a => prev = [1,1,2,2,3]
            if a == 1:
                prev[-1] += 1
                total += 1
            else:  # a = 0
                if len(prev) < k+1:
                    prev[-1] += 1
                    prev.append(0)
                    total += 1
                else:  # len(prev) = k+1
                    if k > 0:
                        total -= prev.popleft()-1
                        prev[-1] += 1
                        prev.append(0)
                    else:
                        total = prev[-1] = 0
            longest = max(longest, total)
        return longest

# Runtime = 56 ms  Beats 80.11% ; Memory = 18.36 MB  Beats 40.75%
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = zeros = l = 0
        for r in range(len(nums)):
            # Инваринат цикла:
            # для данного r число l = минимальное число 0 <= l <= r такое, что nums[l..r-1] содержит (zeros <= k) нулей.
            # примечание: nums[l..r-1] может быть пустым если l = r
            # Теперь нужно найти новое l для nums[l..r]
            if nums[r] == 0:
                zeros += 1
                while zeros > k:
                    if nums[l] == 0: zeros -= 1
                    l += 1
            longest = max(longest, r+1-l)
        return longest


sln = Solution()
print(sln.longestOnes(nums=[1,1,1,0,0,0,1,1,1,1,0], k=2))  # Output: 6

sln = Solution()
print(sln.longestOnes(nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3))  # Output: 10

sln = Solution()
print(sln.longestOnes(nums=[0,0,1,1,1,0,0], k=0))  # Output: 3
