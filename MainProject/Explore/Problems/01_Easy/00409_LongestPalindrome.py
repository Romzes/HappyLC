# Easy 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cntr = Counter(s); sum = 0; odd = 0
        for v in cntr.values():
            if v % 2 == 0: sum += v
            else: sum += v-1; odd = 1
        sum += odd
        return sum

sln = Solution()
print(sln.longestPalindrome(s='abccccdd'))

sln = Solution()
print(sln.longestPalindrome(s='a'))
