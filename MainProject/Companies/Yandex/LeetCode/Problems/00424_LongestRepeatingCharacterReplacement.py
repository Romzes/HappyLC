class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass

sln = Solution()  # Example 1
print(sln.characterReplacement(s='ABAB', k=2))  # Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

sln = Solution()  # Example 2
print(sln.characterReplacement(s='AABABBA', k=1))  # Output: 4
""" Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""