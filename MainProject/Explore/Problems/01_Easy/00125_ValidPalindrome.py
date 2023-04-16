# Easy 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# in-place two-pointer
class Solution:
    def isPalindrome(self, s):
        i = 0; j = len(s)-1
        while i < j:
            if not s[i].isalnum(): i += 1
            elif not s[j].isalnum(): j -= 1
            else:
                if s[i].lower() != s[j].lower(): return False
                i += 1; j -= 1
        return True

sln = Solution()
print(sln.isPalindrome(s='0P'))

sln = Solution()
print(sln.isPalindrome(s='a'))

sln = Solution()
print(sln.isPalindrome(s='a b1a'))

sln = Solution()
print(sln.isPalindrome(s='aba'))

sln = Solution()
print(sln.isPalindrome(s='A man, a plan, a canal: Panama'))

sln = Solution()
print(sln.isPalindrome(s='race a car'))