# Medium 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums, target):
        ti = self.search(nums, i1=0, i2=len(nums)-1, target=target, dir='')
        if ti == -1: return [-1, -1]
        rng = [ti, ti]
        if ti > 0 and nums[ti-1] == target:
            rng[0] = self.search(nums, i1=0, i2=ti-1, target=target, dir='L')
        if ti < len(nums)-1 and nums[ti+1] == target:
            rng[1] = self.search(nums, i1=ti+1, i2=len(nums)-1, target=target, dir='R')
        return rng

    def search(self, nums, i1, i2, target, dir):
        # dir = '', 'L', 'R'
        ti = -1
        while i1 <= i2:
            mi = int((i1 + i2)/2); mv = nums[mi]
            if target < mv: i2 = mi-1
            elif mv < target: i1 = mi+1
            elif mv == target:
                ti = mi
                if dir == '': break
                if dir == 'L': i2 = mi-1
                elif dir == 'R': i1 = mi+1
        return ti

sln = Solution()
print(sln.searchRange(nums=[5,7,7,8,8,10], target=8))

sln = Solution()
print(sln.searchRange(nums=[5,7,7,8,8,10], target=6))

sln = Solution()
print(sln.searchRange(nums=[], target=0))
