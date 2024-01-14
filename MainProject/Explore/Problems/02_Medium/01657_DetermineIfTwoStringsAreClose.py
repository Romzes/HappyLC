"""
1657. (Medium) Determine if Two Strings Are Close
Two strings are considered close if you can attain one from the other using the following operations:
Operation 1: Swap any two existing characters.
  For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
  For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
Constraints:
  1 <= word1.length, word2.length <= 10^5
  word1 and word2 contain only lowercase English letters.
"""

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2): return False
        return Counter(Counter(word1).values()) == Counter(Counter(word2).values())


sln = Solution()
print(sln.closeStrings(word1='abc', word2='bca'))

sln = Solution()
print(sln.closeStrings(word1='a', word2='aa'))

sln = Solution()
print(sln.closeStrings(word1='cabbba', word2='abbccc'))