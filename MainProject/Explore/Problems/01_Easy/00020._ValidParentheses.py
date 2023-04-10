# Easy 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s):
        stack, open, close = [], '({[', {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in open: stack.append(c)
            else:
                if not stack or stack.pop() != close[c]: return False
        return len(stack) == 0

sln = Solution()
print(sln.isValid(s='()'))

sln = Solution()
print(sln.isValid(s='()[]{}'))

sln = Solution()
print(sln.isValid(s='(]'))