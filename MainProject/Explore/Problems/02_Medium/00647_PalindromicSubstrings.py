"""
647 (Medium) Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
Constraints:
  1 <= s.length <= 1000
  s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0; n = len(s)
        for i in range(n):
            j1 = j2 = i
            while 0 <= j1 and j2 < n and s[j1] == s[j2]:
                res += 1; j1 -= 1; j2 += 1
            j1 = i; j2 = i+1
            while 0 <= j1 and j2 < n and s[j1] == s[j2]:
                res += 1; j1 -= 1; j2 += 1
        return res

sln = Solution()
print(sln.countSubstrings(s='abc'))

sln = Solution()
print(sln.countSubstrings(s='aaa'))