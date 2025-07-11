# 605 (Easy) Can Place Flowers
"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Constraints:
  1 <= flowerbed.length <= 2 * 10^4
  flowerbed[i] is 0 or 1.
  There are no two adjacent flowers in flowerbed.
  0 <= n <= flowerbed.length
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        k = 0
        for i, b in enumerate(flowerbed):
            if b == 1: continue
            if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                k += 1
                if k == n: return True
        return False


sln = Solution()
print(sln.canPlaceFlowers(flowerbed=[1,0,0,0,1], n=1))  # Output: true

sln = Solution()
print(sln.canPlaceFlowers(flowerbed=[1,0,0,0,1], n=2))  # Output: false