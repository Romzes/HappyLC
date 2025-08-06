class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(t) - len(s)) > 1: return False
        if len(s) > len(t): s, t = t, s
        # len(s) <= len(t)
        err_cnt = 0
        i = j = 0
        while i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            err_cnt += 1
            if err_cnt > 1: return False
            if len(s) == len(t): i += 1
            j += 1
        return err_cnt == 1 or len(s) < len(t)


sln = Solution()  # Example 1
print(sln.isOneEditDistance(s='ab', t='acb'))  # Output: true

sln = Solution()  # Example 2
print(sln.isOneEditDistance(s='', t=''))  # Output: false
# Explanation: We cannot get t from s by only one step.

sln = Solution()
print(sln.isOneEditDistance(s='', t=''))  # Output: false

sln = Solution()
print(sln.isOneEditDistance(s='a', t=''))  # Output: true



