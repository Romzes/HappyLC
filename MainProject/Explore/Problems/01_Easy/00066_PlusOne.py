"""
66 (Easy) Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Constraints:
  1 <= digits.length <= 100
  0 <= digits[i] <= 9
  digits does not contain any leading 0's.
"""
from typing import List

# Runtime 44 ms , Beats 21.14% of users with Python3
# Memory 16.46 MB , Beats 81.76% of users with Python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits); res = n*[0]; a = 1
        for i in range(n-1, -1, -1): a, res[n-1-i] = divmod(digits[i] + a, 10)
        if a == 1: res.append(1)
        res.reverse()
        return res

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits); res = []; a = 1
        for i in range(n-1, -1, -1):
            d = digits[i] + a
            if d <= 9:
                res.append(d)
                for j in range(i-1, -1, -1): res.append(digits[j])
                break
            else:
                res.append(0)
                a = 1
        else: res.append(1)
        res.reverse()
        return res

sln = Solution()
print(sln.plusOne(digits=[1,2,3]))

sln = Solution()
print(sln.plusOne(digits=[4,3,2,1]))

sln = Solution()
print(sln.plusOne(digits=[9]))

