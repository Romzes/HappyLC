# 784 (Medium) Letter Case Permutation
"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.
Return the output in any order.

Constraints:
  1 <= s.length <= 12
  s consists of lowercase English letters, uppercase English letters, and digits.
"""

from typing import List

# Runtime = 7ms  Beats 45.11%  ;  Memory = 18.60MB  Beats 70.53%
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.s_arr = list(s)
        self.res_list = []
        self.backtrack(start_ind=0)
        return self.res_list

    def backtrack(self, start_ind):
        for i in range(start_ind, len(self.s_arr)):
            c = self.s_arr[i]
            if c.isalpha():
                self.s_arr[i] = c.swapcase()
                self.backtrack(start_ind=i+1)
                self.s_arr[i] = c
        self.res_list.append(''.join(self.s_arr))

sln = Solution()
res_list = sln.letterCasePermutation(s="a1b2")
print(len(res_list), res_list)  # Output: ["a1b2","a1B2","A1b2","A1B2"]

sln = Solution()
res_list = sln.letterCasePermutation(s="3z4")
print(len(res_list), res_list)  # Output: ["3z4","3Z4"]

