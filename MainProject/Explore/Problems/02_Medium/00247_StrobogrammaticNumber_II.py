"""
247. (Medium) Strobogrammatic Number II
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Constraints:
  1 <= n <= 14
"""

from typing import List
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        dig_arr = ['0', '1', '8', '6', '9']
        dig_cnt = len(dig_arr)
        dig_map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        m, k = divmod(n, 2)
        for k1 in range(3**k):
            for i in range(int(dig_cnt**(m-1)), int(dig_cnt**m)):
                seq = n*[0]
                if k == 1: seq[m] = dig_arr[k1]
                d = i
                for j in range(m-1, -1, -1):
                    d, r = divmod(d, dig_cnt)
                    seq[j] = dig_arr[r]
                    seq[n-1-j] = dig_map[seq[j]]
                res.append(''.join(seq))
        return res

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dig_map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        m, r = divmod(n, 2)
        result = ['0', '1', '8'] if r == 1 else ['']
        for i in range(m):
            result = [d + seq + dig_map[d] for seq in result for d in dig_map if not(d == '0' and i == m-1)]
        return result

sln = Solution()
print(sln.findStrobogrammatic(n=1))

sln = Solution()
print(sln.findStrobogrammatic(n=2))

sln = Solution()
print(sln.findStrobogrammatic(n=3))