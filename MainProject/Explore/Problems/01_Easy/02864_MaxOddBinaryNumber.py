"""
2864 (Easy) Maximum Odd Binary Number
You are given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
Return a string representing the maximum odd binary number that can be created from the given combination.
Note that the resulting string can have leading zeros.
Constraints:
  1 <= s.length <= 100
  s consists only of '0' and '1'.
  s contains at least one '1'.
"""
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = len(s) * ['1']; i = len(s)-2
        for c in s:
            if c == '0':
                res[i] = '0'
                i -= 1
        return ''.join(res)

sln = Solution()
print(sln.maximumOddBinaryNumber(s='010'))

sln = Solution()
print(sln.maximumOddBinaryNumber(s='0101'))