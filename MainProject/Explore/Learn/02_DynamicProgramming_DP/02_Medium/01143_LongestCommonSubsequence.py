# Medium 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

##### dp = matrix [m x n]
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        ### string intersection
        chars = set(text1).intersection(set(text2))
        if len(chars) == 0: return 0
        text1 = ''.join(c for c in text1 if c in chars)
        text2 = ''.join(c for c in text2 if c in chars)
        ### Main Solution
        n = len(text1); m = len(text2); dp = [m*[0] for _ in text1]
        ### dp[0][0..m-1]
        j2 = text2.find(text1[0])
        for j in range(j2, m): dp[0][j] = 1
        ### dp[0..n-1][0]
        i1 = text1.find(text2[0])
        for i in range(i1, n): dp[i][0] = 1
        ### dp[1..n-1][1..m-1]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if text1[i] != text2[j] else 1 + dp[i-1][j-1]

        return dp[n-1][m-1]

##### Memory Optimization dp
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        ### string intersection
        chars = set(text1).intersection(set(text2))
        if len(chars) == 0: return 0
        text1 = ''.join(c for c in text1 if c in chars)
        text2 = ''.join(c for c in text2 if c in chars)
        ### Main Solution
        n = len(text1); m = len(text2);  # dp = [m*[0] for _ in text1]
        prev_row = m*[0]  # = dp[0][0..m-1]
        j2 = text2.find(text1[0])
        for j in range(j2, m): prev_row[j] = 1
        i1 = text1.find(text2[0])
        # for i in range(i1, n): dp[i][0] = 1
        ### dp[1..n-1][0..m-1]
        for i in range(1, n):
            curr_row = m*[0]  # = dp[i][0..m-1]
            for j in range(0, m):
                if j == 0 and i >= i1: curr_row[j] = 1
                else: curr_row[j] = max(prev_row[j], curr_row[j-1]) if text1[i] != text2[j] else 1 + prev_row[j-1]
            prev_row = curr_row

        return prev_row[m-1]

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


