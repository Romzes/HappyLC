# 215 (Medium) Kth Largest Element in an Array
"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Constraints:
  1 <= k <= nums.length <= 10^5
  -10^4 <= nums[i] <= 10^4
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []  # heap
        for a in nums:
            if len(hp) < k:
                hp.append(a)
                if len(hp) == k: heapq.heapify(hp)
                continue
            if a <= hp[0]: continue
            heapq.heappushpop(hp, a)
        return hp[0]


sln = Solution()
print(sln.findKthLargest(nums=[3,2,1,5,6,4], k=2))

sln = Solution()
print(sln.findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4))