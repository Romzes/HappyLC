# Easy 2215. Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#   answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#   answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

class Solution:
    def findDifference(self, nums1, nums2):
        st1 = set(nums1); st2 = set(nums2)
        return [list(st1-st2), list(st2-st1)]

sln = Solution()
print(sln.findDifference(nums1=[1,2,3], nums2=[2,4,6]))

sln = Solution()
print(sln.findDifference(nums1=[1,2,3,3], nums2=[1,1,2,2]))