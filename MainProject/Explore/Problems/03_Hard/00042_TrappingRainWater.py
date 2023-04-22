# Hard 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

class Solution:
    def trap(self, height):
        if not height or len(height) <= 2: return 0
        m1 = m2 = float('-inf'); water = len(height)*[0]; s = 0
        for i in range(1, len(height)-1):
            m1 = max(m1, height[i-1])
            water[i] = m1
        for i in range(len(height)-2, 0, -1):
            m2 = max(m2, height[i+1])
            water[i] = max(0, min(m2, water[i]) - height[i])
            s += water[i]
        return s

sln = Solution()
print(sln.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))

sln = Solution()
print(sln.trap(height=[4,2,0,3,2,5]))