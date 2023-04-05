# Medium 2439. Minimize Maximum of Array
# You are given a 0-indexed array nums comprising of n non-negative integers.
# In one operation, you must:
#     Choose an integer i such that 1 <= i < n and nums[i] > 0.
#     Decrease nums[i] by 1.
#     Increase nums[i - 1] by 1.
# Return the minimum possible value of the maximum integer of nums after performing any number of operations.

import math
class Solution:
    def minimizeArrayValue(self, nums):
        mx = s = nums[0]
        for i in range(1, len(nums)):
            s += nums[i]
            if nums[i] <= mx: continue
            mx = max(mx, math.ceil(s / (i+1)))
        return mx

sln = Solution()
# print(sln.minimizeArrayValue(nums=[4,0,5,1,8,6]))
print(sln.minimizeArrayValue(nums=[4,7,2,2,9,19,16,0,3,15]))