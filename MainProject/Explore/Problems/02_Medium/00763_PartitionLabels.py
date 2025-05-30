# 763 (Medium) Partition Labels
# Hash Table | Two Pointers | String | Greedy
"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Constraints:
  1 <= s.length <= 500
  s consists of lowercase English letters
"""

from typing import List

# Runtime = 3 ms  Beats = 91.03% ; Memory = 17.61 MB  Beats = 84.49%
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ord_a = ord('a')
        last = 26 * [-1]
        for i, c in enumerate(s): last[ord(c)-ord_a] = i
        res = []
        j1 = j2 = 0  # current part
        for i, c in enumerate(s):
            # j1 <= i <= j2
            j2 = max(j2, last[ord(c)-ord_a])
            if i == j2:
                res.append(j2-j1+1)
                j1 = j2 = i+1
        return res

# Runtime = 7 ms  Beats = 40.3% ; Memory = 17.84 MB  Beats = 34.78%
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        res = []
        j1 = j2 = 0  # current part
        for i, c in enumerate(s):
            # j1 <= i <= j2
            j2 = max(j2, last[c])
            if i == j2:
                res.append(j2-j1+1)
                j1 = j2 = i+1
        return res


sln = Solution()
print(sln.partitionLabels(s='ababcbacadefegdehijhklij'))

sln = Solution()
print(sln.partitionLabels(s='eccbbbbdec'))