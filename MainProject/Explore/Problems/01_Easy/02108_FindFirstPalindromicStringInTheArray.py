"""
2108 (Easy) Find First Palindromic String in the Array
Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
Constraints:
  1 <= words.length <= 100
  1 <= words[i].length <= 100
  words[i] consists only of lowercase English letters.
"""
from typing import List

# Runtime 84 ms , Beats 39.39% of users with Python3
# Memory 16.86 MB , Beats 51.44% of users with Python3
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.is_pal(w): return w
        return ''

    def is_pal(self, w):
        i, j = 0, len(w)-1
        while i < j:
            if w[i] != w[j]: return False
            i, j = i+1, j-1
        return True

# Runtime 79 ms , Beats 55.34% of users with Python3
# Memory 16.81 MB , Beats 51.44% of users with Python3
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            i, j = 0, len(w)-1
            while i < j:
                if w[i] != w[j]: break
                i += 1; j -=1
            else: return w
        return ''

# Runtime 75 ms , Beats 72.60% of users with Python3
# Memory 16.83 MB , Beats 51.44% of users with Python3
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]: return w
        return ''

sln = Solution()
words = ["abc","car","ada","racecar","cool"]
print(sln.firstPalindrome(words))

sln = Solution()
words = ["notapalindrome","racecar"]
print(sln.firstPalindrome(words))

sln = Solution()
words = ["def","ghi"]
print(sln.firstPalindrome(words))