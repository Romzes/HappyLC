from typing import List

# Runtime = O(n) , Memory = O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0
        # n >= 3
        water = 0  # return
        right_max = n * [None]
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1): right_max[i] = max(height[i], right_max[i+1])
        left_max = height[0]
        for i in range(1, n-1):
            water += max(0, min(left_max, right_max[i+1]) - height[i])
            left_max = max(left_max, height[i])
        return water

# Runtime = O(n) , Memory = O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0
        # n >= 3
        water = 0  # return
        left_max, right_max = height[0], height[n-1]
        i, j = 1, n-2
        while i <= j:
            if left_max <= right_max:
                water += max(0, left_max - height[i])
                left_max = max(left_max, height[i])
                i += 1
            else:
                water += max(0, right_max - height[j])
                right_max = max(right_max, height[j])
                j -= 1
        return water


sln = Solution()  # Example 1
print(sln.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6

sln = Solution()  # Example 2
print(sln.trap(height=[4,2,0,3,2,5]))  # Output: 9