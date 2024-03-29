"""
1239 (Medium) Maximum Length of a Concatenated String with Unique Characters
You are given an array of strings arr.
A string s is formed by the concatenation of a subsequence of arr that has unique characters.
Return the maximum possible length of s.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
Constraints:
  1 <= arr.length <= 16
  1 <= arr[i].length <= 26
  arr[i] contains only lowercase English letters.
"""
import string
from typing import List

class Solution:
    # Dinar
    def maxLength(self, arr: List[str]) -> int:
        nums = set()
        def convert(s):
            n = 0
            for char in s:
                idx = 1 << (ord(char) - ord('a'))
                if n & idx:
                    return -1
                n |= idx
            return n
        for s in arr:
            n = convert(s)
            if n != -1 and n not in nums:
                nums.add(n)
        ans = 0
        dp = []
        for n1 in nums:
            for i in range(len(dp)):
                n2 = dp[i]
                if n1 & n2 == 0:
                    new_n = n1 | n2
                    dp.append(new_n)
                    ans = max(ans, new_n.bit_count())
            dp.append(n1)
            ans = max(ans, n1.bit_count())
        print(f'dp = {len(dp)}')
        return ans

class Solution:
    # Roman
    def maxLength(self, arr: List[str]) -> int:
        self.nums = [0]
        for s in arr:
            v = self.s_to_int(s)
            if v != -1: self.nums.append(v)
        if len(self.nums) == 1: return 0
        self.max_len = 0; self.union = len(self.nums) * [0]
        self.rec(i=1)
        return self.max_len

    def rec(self, i):
        if self.max_len == 26 or i == len(self.nums): return
        v, pu = self.nums[i], self.union[i-1]
        cu = pu | v
        if cu == v ^ pu:
            self.union[i] = cu
            self.max_len = max(self.max_len, int.bit_count(cu))
            self.rec(i+1)
        self.union[i] = pu
        self.rec(i+1)

    def s_to_int(self, s):
        v = 0
        for c in s:
            b = 1 << (ord(c) - ord('a'))
            if v & b != 0: return -1
            else: v |= b
        return v

sln = Solution()
print(sln.maxLength(arr=list(string.ascii_lowercase)))

sln = Solution()
print(sln.maxLength(arr=['un', 'iq', 'ue']))

sln = Solution()
print(sln.maxLength(arr=['cha', 'r', 'act', 'ers']))

sln = Solution()
print(sln.maxLength(arr=['abcdefghijklmnopqrstuvwxyz']))