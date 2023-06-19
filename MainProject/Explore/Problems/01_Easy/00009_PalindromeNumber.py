# Easy 9. Palindrome Number
# Given an integer x, return true if x is a palindrome and false otherwise.
# Constraints:
#   -2^31 <= x <= 2^31 - 1
# Follow up: Could you solve it without converting the integer to a string?

### Shortest !!!
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return x==x[::-1]

class Solution:
    def isPalindrome(self, x):
        if x < 0: return False
        if x == 0: return True
        digits = []
        while x > 0:
            x, r = divmod(x, 10)
            digits.append(r)
        i = 0; j = len(digits)-1
        while i < j:
            if digits[i] != digits[j]: return False
            i += 1; j -= 1
        return True

class Solution:
    def isPalindrome(self, x):
        if x < 0: return False
        if x == 0: return True
        digits = []
        while x > 0:
            x, r = divmod(x, 10)
            digits.append(r)
        for i in range(len(digits)//2):
            if digits[i] != digits[len(digits)-1-i]: return False
        return True

sln = Solution()
print(sln.isPalindrome(x=1))

sln = Solution()
print(sln.isPalindrome(x=11))

sln = Solution()
print(sln.isPalindrome(x=121))

sln = Solution()
print(sln.isPalindrome(x=-121))

sln = Solution()
print(sln.isPalindrome(x=10))