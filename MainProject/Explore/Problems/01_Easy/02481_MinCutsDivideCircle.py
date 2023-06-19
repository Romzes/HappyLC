# 2481. Minimum Cuts to Divide a Circle
# A valid cut in a circle can be:
# A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or
# A cut that is represented by a straight line that touches one point on the edge of the circle and its center.
# Some valid and invalid cuts are shown in the figures below.
# Constraints:
# 1 <= n <= 100

class Solution:
    def numberOfCuts(self, n):
        if n == 1: return 0
        d, r = divmod(n, 2)
        return d if r % 2 == 0 else n

sln = Solution()
print(sln.numberOfCuts(n=4))

sln = Solution()
print(sln.numberOfCuts(n=3))