# 347 (Medium) Top K Frequent Elements
"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Constraints:
  1 <= nums.length <= 10^5
  -10^4 <= nums[i] <= 10^4
  k is in the range [1, the number of unique elements in the array].
  It is guaranteed that the answer is unique.
"""

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for a in nums: counter[a] = counter.get(a, 0) + 1
        hp = []  # min-heap
        for a, cnt in counter.items():
            if len(hp) < k:
                hp.append((cnt, a))
                if len(hp) == k: heapq.heapify(hp)
                continue
            if cnt <= hp[0][0]: continue
            heapq.heappushpop(hp, (cnt, a))
        return [t[1] for t in hp]


sln = Solution()
print(sln.topKFrequent(nums=[1,1,1,2,2,3], k=2))

sln = Solution()
print(sln.topKFrequent(nums=[1], k=1))