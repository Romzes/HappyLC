"""
438 (Medium) Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_counter = {}; p_counter = Counter(p)
        res = []; beg = None
        for i, v in enumerate(s):
            s_cnt = s_counter.get(v, 0); p_cnt = p_counter.get(v, 0)
            if p_cnt == 0:
                s_counter.clear()
            elif s_cnt < p_cnt:
                if len(s_counter) == 0: beg = i
                s_counter[v] = s_cnt + 1
                if i - beg + 1 == len(p): res.append(beg)
            else:  # s_cnt == p_cnt
                for j in range(beg, i):
                    if s[j] != v:
                        s_counter[s[j]] -= 1
                    else:
                        beg = j+1
                        if i - beg + 1 == len(p): res.append(beg)
                        break
        return res


sln = Solution()
print(sln.findAnagrams(s='abacbabc', p='abc'))

sln = Solution()
print(sln.findAnagrams(s='cbaebabacd', p='abc'))

sln = Solution()
print(sln.findAnagrams(s='abab', p='ab'))