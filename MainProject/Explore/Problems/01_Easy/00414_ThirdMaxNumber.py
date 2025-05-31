# 414 (Easy) Third Maximum Number
"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
Constraints:
  1 <= nums.length <= 10^4
  -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List
import heapq

# Runtime = 0 ms  Beats 100.00% ; Memory = 18.41 MB  Beats 80.43%
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hp = []
        k = 3
        for a in nums:
            if a in hp: continue
            if len(hp) < k:
                hp.append(a)
                if len(hp) == k: heapq.heapify(hp)
                continue
            # (a not in hp) and len(hp) == k and hp is heap-array
            if a <= hp[0]: continue
            heapq.heappushpop(hp, a)
        return max(hp) if len(hp) < k else hp[0]

# Runtime = 2 ms  Beats 37.12% ; Memory = 18.32 MB  Beats 89.43%
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hp = []
        k = 3
        for a in nums:
            if a in hp: continue
            if len(hp) < k:
                heapq.heappush(hp, a)
                continue
            # (a not in hp) and len(hp) == k and hp is heap-array
            if a <= hp[0]: continue
            heapq.heappushpop(hp, a)
        return max(hp) if len(hp) < k else hp[0]

sln = Solution()
print(sln.thirdMax(nums=[3,2,1]))

sln = Solution()
print(sln.thirdMax(nums=[1,2]))

sln = Solution()
print(sln.thirdMax(nums=[2,2,3,1]))