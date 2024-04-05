"""
1544 (Easy) Make The String Great
"""
import string

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

# Runtime=33ms Beats 83.07% of users with Python3
# Memory=16.81MB Beats 11.30% of users with Python3
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1].lower() == c.lower() and stack[-1] != c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

sln = Solution()
print(sln.makeGood(s='leEeetcode'))

sln = Solution()
print(sln.makeGood(s='abBAcC'))

sln = Solution()
print(sln.makeGood(s='s'))

# for i, c in enumerate(string.ascii_lowercase): print(ord(string.ascii_uppercase[i]) - ord(c))
