# Easy 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s):
        brackets, stack = {'(':')', '{':'}', '[':']'}, []
        for c in s:
            if c in brackets: stack.append(c)
            else:
                if not stack or brackets[stack.pop()] != c: return False
        return len(stack) == 0

sln = Solution()
print(sln.isValid(s='()'))

sln = Solution()
print(sln.isValid(s='()[]{}'))

sln = Solution()
print(sln.isValid(s='(]'))