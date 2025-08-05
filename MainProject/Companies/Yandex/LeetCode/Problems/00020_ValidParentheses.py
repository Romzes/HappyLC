class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open, close = '([{', ')]}'
        for c in s:
            if c in open:
                stack.append(c)
                continue
            i = close.find(c)
            if i != -1:
                if not stack or stack[-1] != open[i]: return False
                stack.pop()
        return len(stack) == 0

class Solution:
    def isValid(self, s):
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in brackets: stack.append(c)
            else:
                if not stack or brackets[stack.pop()] != c: return False
        return len(stack) == 0


sln = Solution()  # Example 1
print(sln.isValid(s='()'))  # Output: true

sln = Solution()  # Example 2
print(sln.isValid(s='()[]{}'))  # Output: true

sln = Solution()  # Example 3
print(sln.isValid(s='(]'))  # Output: false

sln = Solution()  # Example 4
print(sln.isValid(s='([])'))  # Output: true

sln = Solution()  # Example 5
print(sln.isValid(s='([)]'))  # Output: false
