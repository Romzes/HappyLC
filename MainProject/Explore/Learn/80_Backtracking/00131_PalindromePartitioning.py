# 131 (Medium) Palindrome Partitioning
"""
Given a string s, partition s such that every substring  of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Constraints:
  1 <= s.length <= 16
  s contains only lowercase English letters.
"""

from typing import List
from collections import defaultdict

# Runtime = 47ms  Beats 71.47%  ;  Memory = 32.71 MB  Beats 86.98%
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.pals = self.find_palindromes(s)
        self.comb = []  # комбинация палиндромов
        self.res_list = []
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        if start_ind == len(self.s):
            self.res_list.append(self.comb[::])
            return
        for i in range(start_ind, len(self.s)):
            indexes = self.pals.get(start_ind)
            if i - start_ind == 0 or (indexes and i in indexes):
                pal = self.s[start_ind:i+1]  # pal - palindrome
                self.comb.append(pal)
                self.backtrack(start_ind=i+1)
                self.comb.pop()

    def find_palindromes(self, s):
        pals = defaultdict(set)  # {i: [j_1,...,j_k]}
        m = len(s)
        for i in range(m-1):
            j1, j2 = i, i+1
            while 0 <= j1 and j2 < m and s[j1] == s[j2]:
                pals[j1].add(j2)
                j1 -= 1
                j2 += 1
        for i in range(1, m-1):
            j1, j2 = i-1, i+1
            while 0 <= j1 and j2 < m and s[j1] == s[j2]:
                pals[j1].add(j2)
                j1 -= 1
                j2 += 1
        return pals


# Runtime = 48ms  Beats 63.08%  ;  Memory = 32.62MB  Beats 91.13%
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.comb = []  # комбинация палиндромов
        self.res_list = []
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        # start_ind = index of string s
        if start_ind == len(self.s):
            self.res_list.append(self.comb[::])
            return
        for i in range(start_ind, len(self.s)):
            pal = self.s[start_ind:i+1]
            if pal == pal[::-1]:
                # pal = palindrome
                self.comb.append(pal)
                self.backtrack(start_ind=i+1)
                self.comb.pop()


sln = Solution()
partition = sln.res_list(s='aab')
print(len(partition), partition)
# Output: [["a","a","b"],["aa","b"]]

sln = Solution()
partition = sln.res_list(s='a')
print(len(partition), partition)
# Output: [["a"]]