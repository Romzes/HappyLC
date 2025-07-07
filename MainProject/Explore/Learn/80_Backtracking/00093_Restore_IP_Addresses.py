# 93 (Medium) Restore IP Addresses
'''
A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
For example:
  valid   IP addresses - '0.1.2.201' , '192.168.1.1'
  invalid IP addresses - '0.011.255.245' , '192.168.1.312' , '192.168@1.1'

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s.
You may return the valid IP addresses in any order.

Constraints:
  1 <= s.length <= 20
  s consists of digits only.
'''

from typing import List

# Runtime = 0ms  Beats 100.00%  ;  Memory = 17.90MB  Beats 48.28%
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        self.comb = []  # = list[int-str]
        self.res_list = []
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        # 0 <= start_ind <= len(s)
        if start_ind == len(self.s) or len(self.comb) == 4:
            if start_ind == len(self.s) and len(self.comb) == 4: self.res_list.append('.'.join(self.comb))
            return

        min_len = len(self.s) - start_ind - 3 * (3 - len(self.comb))
        for j in range(1, 4):
            next_ind = start_ind + j
            if next_ind > len(self.s): return
            v = self.s[start_ind:next_ind]
            if (v[0] == '0' and 1 < len(v)) or 255 < int(v): return
            if len(v) < min_len: continue
            self.comb.append(v)
            self.backtrack(start_ind=next_ind)
            self.comb.pop()


sln = Solution()
print(sln.restoreIpAddresses(s='25525511135'))  # Output: ['255.255.11.135', '255.255.111.35']

sln = Solution()
print(sln.restoreIpAddresses(s='0000'))  # Output: ['0.0.0.0']

sln = Solution()
print(sln.restoreIpAddresses(s='101023'))  # Output: ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']