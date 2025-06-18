# 415 (Easy) Add Strings
"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.
Constraints:
  1 <= num1.length, num2.length <= 10^4
  num1 and num2 consist of only digits.
  num1 and num2 don't have any leading zeros except for the zero itself.
"""

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.14 MB  Beats 55.49%
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ord_0 = ord('0')
        i, j = len(num1)-1, len(num2)-1
        add = []  # list[int]
        carry = 0
        while i >= 0 or j >= 0:
            t1 = ord(num1[i]) - ord_0 if i >= 0 else 0
            t2 = ord(num2[j]) - ord_0 if j >= 0 else 0
            carry, p = divmod(t1 + t2 + carry, 10)
            add.append(str(p))
            i -= 1; j -= 1
        if carry == 1: add.append('1')
        # return ''.join(add)[::-1]
        return ''.join(add[i] for i in range(len(add)-1,-1,-1))


sln = Solution()
print(sln.addStrings(num1='11', num2='123'))  # Output: '134'

sln = Solution()
print(sln.addStrings(num1='456', num2='77'))  # Output: '533''

sln = Solution()
print(sln.addStrings(num1='0', num2='0'))  # Output: '0'