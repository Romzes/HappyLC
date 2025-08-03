from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height)-1
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] <= height[j]: i += 1
            else: j -= 1
        return max_area


""" Доказательство
индексы i, j : 0 <= i < j <= n-1
объём воды V(i, j) = (j - i) * min(height[i], height[j])
пусть height[i] <= height[j] => V(i, j) >= V(i, j1) где i < j1 < j
    т.к. min(height[i], height[j]) = height[i] >= min(height[i], height[j1])
    
рассмотрим треугольник 0 <= i < j <= n-1 всех возможных пар
на каждой итерации из этого треугольника вычеркивается либо левый столбец, либо верхняя строка
"""

sln = Solution()  # Example 1
print(sln.maxArea(height=[1,8,6,2,5,4,8,3,7]))  # Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

sln = Solution()  # Example 2
print(sln.maxArea(height=[1,1]))  # Output: 1
