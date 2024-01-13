"""
1704. (Easy) Determine if String Halves Are Alike
You are given a string s of even length.
Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.
Constraints:
  2 <= s.length <= 1000
  s.length is even.
  s consists of uppercase and lowercase letters.
"""
from typing import Optional

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU'); cnt = 0; m = len(s) // 2
        for i, c in enumerate(s):
            if c in vowels: cnt += 1 if i < m else -1
        return cnt == 0

sln = Solution()
print(sln.halvesAreAlike(s='book'))

sln = Solution()
print(sln.halvesAreAlike(s='textbook'))

sln = Solution()
print(sln.halvesAreAlike(s='AbCdEfGh'))