"""
2870. (Medium) Minimum Number of Operations to Make Array Empty
You are given a 0-indexed array nums consisting of positive integers.
There are two types of operations that you can apply on the array any number of times:
  Choose two elements with equal values and delete them from the array.
  Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
Constraints:
  2 <= nums.length <= 10^5
  1 <= nums[i] <= 10^6
"""

class Solution:
    def minOperations(self, nums):
        nums.sort()
        res = cnt = 0
        opers = [0, -1, 1, 1, 2]  # index = cnt
        for i, v in enumerate(nums):
            cnt += 1
            if i == len(nums)-1 or v != nums[i+1]:
                if cnt == 1: return -1
                if cnt >= len(opers):
                     for j in range(len(opers), cnt+1):
                         opers.append(1 + min(opers[j-2], opers[j-3]))
                res += opers[cnt]
                cnt = 0
        return res

sln = Solution()
print(sln.minOperations(nums=[2,3,3,2,2,4,2,3,4]))

sln = Solution()
print(sln.minOperations(nums=[2,1,2,2,3,3]))