# Easy 1502. Can Make Arithmetic Progression From Sequence
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

class Solution:
    def canMakeArithmeticProgression(self, arr):
        n = len(arr)
        if n <= 2: return True
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(n-1):
            if arr[i+1] - arr[i] != d: return False
        return True

sln = Solution()
arr = [3,5,1]
print(sln.canMakeArithmeticProgression(arr))

sln = Solution()
arr = [1,2,4]
print(sln.canMakeArithmeticProgression(arr))