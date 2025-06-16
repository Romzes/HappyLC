# 11 (Medium) Container With Most Water
"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant-наклонять the container.

Constraints:
  n == height.length
  2 <= n <= 10^5
  0 <= height[i] <= 10^4
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_s = 0
        i, j = 0, len(height)-1
        while i < j:
            curr_s = (j - i) * min(height[i], height[j])
            max_s = max(max_s, curr_s)
            if height[i] <= height[j]: i += 1
            else: j -= 1
        return max_s


sln = Solution()
print(sln.maxArea(height=[1,8,6,2,5,4,8,3,7]))  # Output: 49

sln = Solution()
print(sln.maxArea(height=[1,1]))  # Output: 1