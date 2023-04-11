# Medium 2390. Removing Stars From a String
# You are given a string s, which contains stars *.
# In one operation, you can:
#     Choose a star in s.
#     Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# Note:
#     The input will be generated such that the operation is always possible.
#     It can be shown that the resulting string will always be unique.

# Stack
class Solution:
    def removeStars(self, s):
        # s: str
        stack = []
        for c in s:
            if c != '*': stack.append(c)
            else: stack.pop()
        return ''.join(stack)

# List
class Solution2:
    def removeStars(self, s):
        # s: list
        j = 0
        for i, c in enumerate(s):
            if c != '*': s[j], j = c, j+1
            else: j -= 1
        return s[0:j]



sln = Solution()
print(sln.removeStars(s='leet**cod*e'))

sln = Solution()
print(sln.removeStars(s='erase*****'))


sln = Solution2()
print(sln.removeStars(s=list('leet**cod*e')))

sln = Solution2()
print(sln.removeStars(s=list('erase*****')))

sln = Solution2()
print(sln.removeStars(s=list('ab*cd*efg**')))