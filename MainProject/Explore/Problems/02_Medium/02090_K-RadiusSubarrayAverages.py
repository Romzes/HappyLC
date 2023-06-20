# Medium 2090. K Radius Subarray Averages
# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k
# is the average of all elements in nums between the indices i - k and i + k (inclusive).
# If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x, using integer division.
# The integer division truncates toward zero, which means losing its fractional part.
# Constraints:
#   n == nums.length
#   1 <= n <= 10^5
#   0 <= nums[i], k <= 10^5

class Solution:
    def getAverages(self, nums, k):
        if k == 0: return nums
        n = len(nums); avgs = n*[-1]; m=2*k+1
        if n < m: return avgs
        s = 0
        for i in range(m): s += nums[i]
        avgs[k] = s // m
        j1 = 0; j2 = m
        for i in range(k+1, n-k):
            s += nums[j2] - nums[j1]
            avgs[i] = s // m
            j1 += 1; j2 += 1
        return avgs

sln = Solution()
print(sln.getAverages(nums=[7,4,3,9,1,8,5,2,6], k=3))

sln = Solution()
print(sln.getAverages(nums=[100000], k=0))

sln = Solution()
print(sln.getAverages(nums=[8], k=100000))