# 480 (Hard) Sliding Window Median
"""
The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle values.
  For examples, if arr = [2,3,4], the median is 3.
  For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.

You are given an integer array nums and an integer k.
There is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the median array for each window in the original array.
Answers within 10-5 of the actual value will be accepted.

Constraints:
  1 <= k <= nums.length <= 10^5
  -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap, min_heap = [], []  # max_heap < min_heap
        for i in range(k, len(nums)):
            c = nums[i]
            a, b = nums[i], nums[i-k]

sln = Solution()
print(sln.medianSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3))  # Output: [1,-1,-1,3,5,6]

sln = Solution()
print(sln.medianSlidingWindow(nums=[1,2,3,4,2,3,1,4,2], k=3))  # Output: [2,3,3,3,2,3,2]