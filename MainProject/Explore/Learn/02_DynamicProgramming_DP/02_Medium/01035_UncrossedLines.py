# Medium 1035. Uncrossed Lines
# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
#   nums1[i] == nums2[j], and
#   the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
# Return the maximum number of connecting lines we can draw in this way.

class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        self.m1 = len(nums1); self.m2 = len(nums2); self.dp = [self.m2 * [None] for _ in nums1]
        for i in range(self.m1-1, -1, -1):
            for j in range(self.m2-1, -1, -1):
                self.dp[i][j] = 1 + self.dp_val(i+1, j+1) if nums1[i] == nums2[j] else max(self.dp_val(i, j+1), self.dp_val(i+1, j))
        return self.dp[0][0]

    def dp_val(self, i, j):
        return self.dp[i][j] if 0 <= i < self.m1 and 0 <= j < self.m2 else 0

class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        m1 = len(nums1); m2 = len(nums2); curr = (m2+1)*[0]; next = (m2+1)*[0]
        for i in range(m1-1, -1, -1):
            for j in range(m2-1, -1, -1):
                curr[j] = 1 + next[j+1] if nums1[i] == nums2[j] else max(curr[j+1], next[j])
            next, curr = curr, next
        return next[0]


sln = Solution()
print(sln.maxUncrossedLines(nums1=[1,4,2], nums2=[1,2,4]))

sln = Solution()
print(sln.maxUncrossedLines(nums1=[2,5,1,2,5], nums2=[10,5,2,1,5,2]))

sln = Solution()
print(sln.maxUncrossedLines(nums1=[1,3,7,1,7,5], nums2=[1,9,2,5,1]))