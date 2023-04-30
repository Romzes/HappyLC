# Medium 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Could you come up with a one-pass algorithm using only constant extra space?

### Counter, two-pass
class Solution:
    def sortColors(self, nums):
        counter = [0,0,0]
        for v in nums: counter[v] += 1
        i = 0
        for v, cnt in enumerate(counter):
            for _ in range(cnt): nums[i] = v; i += 1

### two-pointers
class Solution:
    def sortColors(self, nums):
        i = 0; j0 = 0; j2 = len(nums)-1
        while i <= j2:
            if nums[i] == 0:
                nums[j0], nums[i] = nums[i], nums[j0]
                j0 += 1
                i += 1
            elif nums[i] == 2:
                nums[j2], nums[i] = nums[i], nums[j2]
                j2 -= 1
            else:
                i += 1


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

