from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = r = 0
        for i in range(len(s)):
            j1, j2 = self.calc_poly_indexes(s, i1=i, i2=i)
            if r - l < j2 - j1: l, r = j1, j2
            j1, j2 = self.calc_poly_indexes(s, i1=i, i2=i+1)
            if r - l < j2 - j1: l, r = j1, j2
        return s[l:r+1]

    def calc_poly_indexes(self, s: str, i1: int, i2: int) -> List[int]:
        # i1 <= i2
        indexes = [-1, -1]
        while 0 <= i1 and i2 < len(s) and s[i1] == s[i2]:
            indexes[0], indexes[1] = i1, i2
            i1 -= 1
            i2 += 1
        return indexes


sln = Solution()  # Example 1
print(sln.longestPalindrome(s='babad'))  # Output: 'bab'
# Explanation: "aba" is also a valid answer.

sln = Solution()  # Example 2
print(sln.longestPalindrome(s='cbbd'))  # Output: 'bb'


