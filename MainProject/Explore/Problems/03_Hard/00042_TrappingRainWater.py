# 42 (Hard) Trapping Rain Water
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Constraints:
  n == height.length
  1 <= n <= 2 * 10^4
  0 <= height[i] <= 10^5
"""

### O(n) space
class Solution:
    def trap(self, height):
        if not height or len(height) <= 2: return 0
        left_water = len(height)*[0]; right_max = s = 0
        for i in range(1, len(height)-1): left_water[i] = max(left_water[i-1], height[i-1])
        for i in range(len(height)-2, 0, -1):
            right_max = max(right_max, height[i+1])
            s += max(0, min(left_water[i], right_max) - height[i])
        return s

### O(1) space, 2-pointers
class Solution:
    def trap(self, height):
        if not height or len(height) <= 2: return 0
        l = 1; r = len(height)-2
        l_max = r_max = s = 0
        while l <= r:
            l_max = max(l_max, height[l-1])
            r_max = max(r_max, height[r+1])
            if l_max <= height[l]: l += 1
            elif height[r] >= r_max: r -= 1
            elif l_max <= r_max:
                s += l_max - height[l]
                l += 1
            else:
                s += r_max - height[r]
                r -= 1
        return s


sln = Solution()
print(sln.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))

sln = Solution()
print(sln.trap(height=[4,2,0,3,2,5]))