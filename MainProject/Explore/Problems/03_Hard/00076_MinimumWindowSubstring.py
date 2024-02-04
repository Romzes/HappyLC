"""
76 (Hard) Minimum Window Substring
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
Constraints:
  m == s.length
  n == t.length
  1 <= m, n <= 10^5
  s and t consist of uppercase and lowercase English letters.
"""
from collections import deque

# Runtime = 71 ms Beats 98.2% of users with Python3
# Memory = 18.74 MB Beats 5.24% of users with Python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}; cnt = len(t)
        for c in t:
            if c not in counter: counter[c] = [0, 0]
            counter[c][0] += 1
        i1 = i2 = None; min_lng = float('+inf')
        dq = deque()
        for i, c in enumerate(s):
            item = counter.get(c)
            if not item: continue
            item[1] += 1
            dq.append(i)
            if item[0] >= item[1]:
                cnt -= 1
                while cnt == 0:
                    j = dq.popleft()
                    item = counter[s[j]]
                    item[1] -= 1
                    if item[0] > item[1]: cnt += 1
                    lng = i - j + 1
                    if lng < min_lng: i1, i2, min_lng = j, i, lng
        return s[i1:(i2+1)] if i1 is not None else ''


# Runtime = 58 ms Beats 99.94% of users with Python3
# Memory = 17.13 MB Beats 90.66% of users with Python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}; cnt = len(t)
        for c in t:
            if c not in counter: counter[c] = [0, 0]
            counter[c][0] += 1
        i1 = i2 = None; min_lng = float('+inf')
        j = -1
        for i, c in enumerate(s):
            item = counter.get(c)
            if not item: continue
            item[1] += 1
            if item[0] >= item[1]:
                cnt -= 1
                while cnt == 0:
                    j += 1
                    item = counter.get(s[j])
                    if not item: continue
                    item[1] -= 1
                    if item[0] > item[1]: cnt += 1
                    lng = i - j + 1
                    if lng < min_lng: i1, i2, min_lng = j, i, lng
        return s[i1:(i2+1)] if i1 is not None else ''

sln = Solution()
print(sln.minWindow(s='ADOBECODEBANC', t='ABC'))

sln = Solution()
print(sln.minWindow(s='a', t='a'))

sln = Solution()
print(sln.minWindow(s='a', t='aa'))