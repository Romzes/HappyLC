from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        digits = []
        while x > 0:
            x, r = divmod(x, 10)
            digits.append(r)
        return self.is_palind(digits)

    def is_palind(self, digits: List[int]) -> bool:
        i, j = 0, len(digits)-1
        while i < j:
            if digits[i] != digits[j]: return False
            i += 1
            j -= 1
        return True

# !!! Follow up: Could you solve it without converting the integer to a string ?

sln = Solution()  # Example 1
print(sln.isPalindrome(x=121))  # Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

sln = Solution()  # Example 2
print(sln.isPalindrome(x=-121))  # Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


sln = Solution()  # Example 3:
print(sln.isPalindrome(x=10))  # Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
