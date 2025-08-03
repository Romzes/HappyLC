class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or s == '': return 0
        res = 0  # return
        start_ind = 0  # начальный индекс текущей строки из уникальных символов
        symbols = {}  # {c: max-index}
        for i, c in enumerate(s):
            j = symbols.get(c)
            if j is not None and start_ind <= j: start_ind = j+1
            symbols[c] = i
            res = max(res, i-start_ind+1)
        return res


sln = Solution()  # Example 1
print(sln.lengthOfLongestSubstring(s='abcabcbb'))  # Output: 3
# Explanation: The answer is "abc", with the length of 3

sln = Solution()  # Example 2
print(sln.lengthOfLongestSubstring(s='bbbbb'))  # Output: 1
# Explanation: The answer is "b", with the length of 1

sln = Solution()  # Example 3
print(sln.lengthOfLongestSubstring(s='pwwkew'))  # Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

sln = Solution()
print(sln.lengthOfLongestSubstring(s='abcdbat'))  # Output: 5



