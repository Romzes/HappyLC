"""
169. (Easy) Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
!!! Follow-up: Could you solve the problem in linear time and in O(1) space? !!!
Constraints:
  n == nums.length
  1 <= n <= 5 * 10^4
  -10^9 <= nums[i] <= 10^9
"""
from typing import List

### простое решение через словарь
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_cnt, max_v = 0, None; counter = {}; m = len(nums) // 2
        for i, v in enumerate(nums):
            c = counter[v] = counter.get(v, 0) + 1
            if max_cnt < c:
                max_cnt, max_v = c, v
                if max_cnt > m: return max_v
        return max_v

### sort сложность = O(n*log(n))
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

sln = Solution()
print(sln.majorityElement(nums=[3,2,3]))

sln = Solution()
print(sln.majorityElement(nums=[2,2,1,1,1,2,2]))