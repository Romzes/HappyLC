# Medium 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Could you come up with a one-pass algorithm using only constant extra space?

### StatCounter
class Solution:
    def sortColors(self, nums):
        stat = [0,0,0]; s = 0
        for v in nums: stat[v] += 1
        for v, cnt in enumerate(stat):
            for i in range(s, s+cnt): nums[i] = v
            s += cnt

sln = Solution()
nums = [2,0,2,1,1,0]
sln.sortColors(nums)
print(nums)

sln = Solution()
nums = [2,0,1]
sln.sortColors(nums)
print(nums)

sln = Solution()
nums = [1,2,0]
sln.sortColors(nums)
print(nums)