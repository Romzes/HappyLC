"""
201 (Medium) Bitwise AND of Numbers Range
Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.
Constraints:
  0 <= left <= right <= 2^31 - 1
"""

# Runtime 43 ms , Beats 90.76% of users with Python3
# Memory 16.60 MB , Beats 81.69% of users with Python3
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 or left == right: return left
        ls, rs = '{0:b}'.format(left), '{0:b}'.format(right)
        # print(ls, rs)
        if len(ls) < len(rs): return 0
        res = len(ls) * ['0']
        for i in range(len(ls)):
            if ls[i] < rs[i]: break
            if ls[i] == rs[i] and rs[i] == '1': res[i] = '1'
        return int(''.join(res), 2)

sln = Solution()
print(sln.rangeBitwiseAnd(left=5, right=7))

sln = Solution()
print(sln.rangeBitwiseAnd(left=0, right=0))

sln = Solution()
print(sln.rangeBitwiseAnd(left=1, right=2147483647))