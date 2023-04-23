# Medium 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

##### Simple
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1); m = len(text2); dp = [m*[0] for _ in text1]; arr = 3*[-1]
        # dp[0][0..m-1]
        j2 = text2.find(text1[0])
        if j2 > -1:
            for j in range(j2, m): dp[0][j] = 1
        # dp[0..n-1][0]
        i1 = text1.find(text2[0])
        if i1 > -1:
            for i in range(i1, n): dp[i][0] = 1
        ### dp[1..n-1][1..m-1]
        for i in range(1, n):
            for j in range(1, m):
                arr[0], arr[1], arr[2] = dp[i-1][j], dp[i][j-1], -1
                if text1[i] == text2[j]: arr[2] = 1 + dp[i-1][j-1]
                dp[i][j] = max(arr)
        return dp[n-1][m-1]

sln = Solution()
print(sln.longestCommonSubsequence(text1='aaa', text2='aa'))

sln = Solution()
print(sln.longestCommonSubsequence(text1='bsbininm', text2='jmjkbkjkv'))

sln = Solution()
print(sln.longestCommonSubsequence(text1='abcde', text2='ace'))

sln = Solution()
print(sln.longestCommonSubsequence(text1='abc', text2='abc'))

sln = Solution()
print(sln.longestCommonSubsequence(text1='abc', text2='def'))

