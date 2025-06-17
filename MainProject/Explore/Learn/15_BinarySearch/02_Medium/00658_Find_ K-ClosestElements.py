# 658 (Medium) Find K Closest Elements
"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
  |a - x| < |b - x|, or
  |a - x| == |b - x| and a < b

Constraints:
  1 <= k <= arr.length
  1 <= arr.length <= 10^4
  arr is sorted in ascending order.
  -10^4 <= arr[i], x <= 10^4
"""

from typing import List

# Runtime = 3 ms  Beats 71.64%  ;  Memory = 19.22 MB  Beats 32.84%
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n <= k: return arr[::]
        i = self.find_closest_index(arr, x)  # arr[i] <= x < arr[i+1]
        j = i+1
        # i будет уменьшаться, j будет увеличиваться
        k_cnt = 0
        while k_cnt < k:
            k_cnt += 1
            if i == -1: return arr[0:k]
            if j == n: return arr[n-k:n]
            if x - arr[i] <= arr[j] - x: i -= 1
            else: j += 1
        return arr[i+1:i+k+1]

    def find_closest_index(self, arr, x):
        i, j = 0, len(arr)-1
        while i <= j:
            m = (i+j) // 2
            v = arr[m]
            if v == x: return m
            if x < v: j = m-1
            else: i = i+1
        return j  # i = j+1


sln = Solution()
print(sln.findClosestElements(arr=[1,2,3,4,5], k=4, x=3))  # Output: [1,2,3,4]

sln = Solution()
print(sln.findClosestElements(arr=[1,1,2,3,4,5], k=4, x=-1))  # Output: [1,1,2,3]