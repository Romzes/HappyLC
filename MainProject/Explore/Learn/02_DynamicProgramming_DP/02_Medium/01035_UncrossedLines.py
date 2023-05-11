from collections import defaultdict

class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        self.m1 = len(nums1); self.m2 = len(nums2); self.dp = [self.m2 * [None] for _ in nums1]
        for i in range(self.m1-1, -1, -1):
            for j in range(self.m2-1, -1, -1):
                self.dp[i][j] = 1 + self.dp_val(i+1, j+1) if nums1[i] == nums2[j] else max(self.dp_val(i, j+1), self.dp_val(i+1, j))
        return self.dp[0][0]

    def dp_val(self, i, j):
        return self.dp[i][j] if 0 <= i < self.m1 and 0 <= j < self.m2 else 0


sln = Solution()
print(sln.maxUncrossedLines(nums1=[1,4,2], nums2=[1,2,4]))

sln = Solution()
print(sln.maxUncrossedLines(nums1=[2,5,1,2,5], nums2=[10,5,2,1,5,2]))

sln = Solution()
print(sln.maxUncrossedLines(nums1=[1,3,7,1,7,5], nums2=[1,9,2,5,1]))