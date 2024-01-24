"""
17 (Medium) Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Constraints:
  0 <= digits.length <= 4
  digits[i] is a digit in the range ['2', '9'].
"""
from typing import List
from copy import deepcopy
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        words = [[]]
        for d in digits:
            chars = chars_dict[d]
            words2 = []
            for w in words:
                for c in chars:
                    w2 = deepcopy(w)
                    w2.append(c)
                    words2.append(w2)
            words = words2
        return [''.join(w) for w in words if len(w) > 0]

sln = Solution()
print(sln.letterCombinations(digits='23'))

sln = Solution()
print(sln.letterCombinations(digits=''))

sln = Solution()
print(sln.letterCombinations(digits='2'))