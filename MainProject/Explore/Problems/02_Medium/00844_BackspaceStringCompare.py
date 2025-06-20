# 844 (Easy) Backspace String Compare
"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
"""

# Runtime = 0 ms   Beats 100.00%  ;  Memory = 17.83 MB  Beats 36.21%
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.transform(s) == self.transform(t)

    def transform(self, s):
        stack = []
        for c in s:
            if c != '#': stack.append(c)
            elif stack: stack.pop()
        return ''.join(stack)


sln = Solution()
print(sln.backspaceCompare(s='ab#c', t='ad#c'))  # Output: true

sln = Solution()
print(sln.backspaceCompare(s='ab##', t='c#d#'))  # Output: true

sln = Solution()
print(sln.backspaceCompare(s='a#c', t='b'))  # false