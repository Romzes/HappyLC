# 3211 (Medium) Generate Binary Strings Without Adjacent Zeros
"""
You are given a positive integer n.
A binary string x is valid if all substrings of x of length 2 contain at least one "1".
Return all valid strings with length n, in any order.

Constraints:
  1 <= n <= 18
"""

from typing import List

# рекурсия
# Runtime = 59ms  Beats 44.11%  ;  Memory = 19.19MB  Beats 71.73%
class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.n = n
        self.res_list = []
        self.comb = []
        self.vars1, self.vars2 = ('1',), ('0', '1')
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        if start_ind == self.n:
            self.res_list.append(''.join(self.comb))
            return
        vars = self.vars2 if (start_ind == 0 or self.comb[-1] == '1') else self.vars1
        for v in vars:
            self.comb.append(v)
            self.backtrack(start_ind=start_ind+1)
            self.comb.pop()

# без рекурсии
# Runtime = 43ms  Beats 98.95%  ;  Memory = 19.48MB  Beats 60.21%
class Solution:
    def validStrings(self, n: int) -> List[str]:
        curr_level = ['0', '1']
        for i in range(n-1):
            next_level = []
            for s in curr_level:
                if s[-1] == '1': next_level.extend((s+'0', s+'1'))
                else: next_level.append(s+'1')
            curr_level = next_level
        return curr_level


sln = Solution()
res_list = sln.validStrings(n=3)
print(len(res_list), res_list)  # Output: ["010","011","101","110","111"]

sln = Solution()
res_list = sln.validStrings(n=1)
print(len(res_list), res_list)  # Output: ["0","1"]
