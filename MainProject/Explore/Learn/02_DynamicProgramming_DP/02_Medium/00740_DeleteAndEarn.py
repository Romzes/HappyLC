# Medium 740. Delete and Earn
# You are given an integer array nums.
# You want to maximize the number of points you get by performing the following operation any number of times:
#   Pick any nums[i] and delete it to earn nums[i] points.
#   Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.
# Constraints:
#   1 <= nums[i]

from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        sum = 0; cntr = Counter(nums); vals = []
        for v, cnt in cntr.items():
            if v-1 not in cntr and v+1 not in cntr: sum += v*cnt
            else: vals.append(v)
        if not vals: return sum
        vals.sort()
        i1 = 0; v1 = vals[0]
        for i2, v2 in enumerate(vals):
            if v2 > v1 + (i2-i1):
                sum += self.calc_seq(vals, i1, i2-1, cntr)
                i1 = i2; v1 = vals[i2]
        sum += self.calc_seq(vals, i1, len(vals)-1, cntr)
        return sum

    def calc_seq(self, vals, i1, i2, cntr):
        a = vals[i1] * cntr[vals[i1]]
        b = max(a, vals[i1+1] * cntr[vals[i1+1]])
        for i in range(i1+2, i2+1): a, b = b, max(b, a + vals[i] * cntr[vals[i]])
        return b

sln = Solution()
print(sln.deleteAndEarn(nums=[3,4,2]))

sln = Solution()
print(sln.deleteAndEarn(nums=[2,2,3,3,3,4]))

sln = Solution()
print(sln.deleteAndEarn(nums=[1,1,1,2,4,5,5,5,6]))

