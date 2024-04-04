"""
1614 (Easy) Maximum Nesting Depth of the Parentheses
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        md = p = 0
        for c in s:
            if c == '(':
                p += 1
                md = max(md, p)
            elif c == ')': p -= 1
        return md

# Runtime=34ms Beats 66.43% of users with Python3
# Memory=16.55MB Beats 38.30% of users with Python3
class Solution:
    def maxDepth(self, s: str) -> int:
        md = p = 0
        for c in s:
            if c == '(': md = max(md, p := p+1)
            if c == ')': p -= 1
        return md

sln = Solution()
print(sln.maxDepth(s='(1+(2*3)+((8)/4))+1'))

sln = Solution()
print(sln.maxDepth(s='(1)+((2))+(((3)))'))