"""
1544 (Easy) Make The String Great
"""
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