# 1422 (Easy) Maximum Score After Splitting a String
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        cnt0 = 0
        cnt1 = sum(int(c) for c in s)
        score = -float('inf')
        for i, c in enumerate(s):
            if i == len(s)-1: break
            if c == '0': cnt0 += 1
            else: cnt1 -= 1
            score = max(score, cnt0+cnt1)
        return score

sln = Solution()
print(sln.maxScore(s='011101'))

sln = Solution()
print(sln.maxScore(s='00111'))

sln = Solution()
print(sln.maxScore(s='1111'))



