# 771 (Easy) Jewels and Stones
"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Constraints:
  1 <= jewels.length, stones.length <= 50
  jewels and stones consist of only English letters.
  All the characters of jewels are unique.
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_set = set(jewels)
        cnt = 0
        for s in stones:
            if s in j_set: cnt += 1
        return cnt

sln = Solution()
print(sln.numJewelsInStones(jewels='aA', stones='aAAbbbb'))  # Output: 3

sln = Solution()
print(sln.numJewelsInStones(jewels='z', stones='ZZ'))  # Output: 0
