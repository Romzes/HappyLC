# 239 (Hard) Sliding Window Maximum
"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
Constraints:
  1 <= nums.length <= 10^5
  -10^4 <= nums[i] <= 10^4
  1 <= k <= nums.length
"""

from typing import List
import heapq
from sortedcontainers import SortedList

# heapq - очень медленное решение
# Runtime = 378 ms = O[n*log(k)]  Beats 14.70%  ;  Memory = 43.42 MB = O[n]  Beats 6.31%
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = (n - k + 1) * [None]
        hp = [(-nums[i], i) for i in range(k)]
        heapq.heapify(hp)
        res[0] = -hp[0][0]
        for i in range(k, n):
            heapq.heappush(hp, (-nums[i], i))
            while hp[0][1] <= i-k: heapq.heappop(hp)
            res[i-k+1] = -hp[0][0]
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = (n - k + 1) * [None]
        sl = SortedList(nums[0:k])
        res[0] = sl[-1]
        for i in range(k, n):
            sl.add(nums[i])
            sl.remove(nums[i-k])
            res[i - k + 1] = sl[-1]
        return res


sln = Solution()
print(sln.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3))  # Output: [3,3,5,5,6,7]

sln = Solution()
print(sln.maxSlidingWindow(nums=[1], k=1))  # Output: [1]