"""
Medium
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.
Constraints:
    1 <= g.length <= 3 * 10^4
    0 <= s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1
"""

class Solution:
    def findContentChildren(self, g, s):
        g.sort(); s.sort(); i = j = ans = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]: ans += 1; i+=1
            j += 1
        return ans

sln = Solution()
print(sln.findContentChildren(g=[1,2,3], s=[1,1]))

sln = Solution()
print(sln.findContentChildren(g=[1,2], s=[1,2,3]))