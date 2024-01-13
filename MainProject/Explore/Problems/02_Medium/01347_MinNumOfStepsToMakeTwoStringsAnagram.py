"""
1347. (Medium) Minimum Number of Steps to Make Two Strings Anagram
You are given two strings of the same length s and t.
In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""
import typing

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0; cnt = {}
        for c in s: cnt[c] = cnt.get(c, 0) + 1
        for c in t: cnt[c] = cnt.get(c, 0) - 1
        for n in cnt.values():
            if n > 0: steps += n
        return steps

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0; cnt = {}
        for c in s: cnt[c] = cnt.get(c, 0) + 1
        for c in t:
            n = cnt.get(c)
            if n is None: steps += 1
            elif n > 1: cnt[c] = n-1
            else: cnt.pop(c)
        return steps

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0; cnt = {}
        for c in s: cnt[c] = cnt.get(c, 0) + 1
        for c in t:
            cnt[c] = cnt.get(c, 0) - 1
            if cnt[c] < 0: steps += 1
        return steps

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0; s_cnt = {}; t_cnt = {}
        for c in s: s_cnt[c] = s_cnt.get(c, 0) + 1
        for c in t: t_cnt[c] = t_cnt.get(c, 0) + 1
        for c, n in s_cnt.items():
            d = n - t_cnt.get(c, 0)
            if d > 0: steps += d
        return steps

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0; s_cnt = Counter(s); t_cnt = Counter(t)
        for c, n in s_cnt.items():
            d = n - t_cnt.get(c, 0)
            if d > 0: steps += d
        return steps

sln = Solution()
print(sln.minSteps(s='bab', t='aba'))

sln = Solution()
print(sln.minSteps(s='leetcode', t='practice'))

sln = Solution()
print(sln.minSteps(s='anagram', t='mangaar'))
