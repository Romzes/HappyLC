"""
392. (Easy) Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Constraints:
  0 <= s.length <= 100
  0 <= t.length <= 10^4
  s and t consist only of lowercase English letters.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s): return True
        return False

sln = Solution()
print(sln.isSubsequence(s='abc', t='ahbgdc'))

sln = Solution()
print(sln.isSubsequence(s='axc', t='ahbgdc'))