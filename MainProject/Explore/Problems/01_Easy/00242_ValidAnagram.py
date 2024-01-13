"""
242. (Easy) Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for c in t:
            m = counter.get(c)
            if not m: return False
            if m == 1: counter.pop(c)
            else: counter[c] = m-1
        return len(counter) == 0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

sln = Solution()
print(sln.isAnagram(s='anagram', t='nagaram'))

sln = Solution()
print(sln.isAnagram(s='rat', t='car'))