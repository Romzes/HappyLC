"""
2225. (Medium) Find Players With Zero or One Losses
You are given an integer array matches where matches[i] = [winner_i, loser_i] indicates that the player winner_i defeated player loser_i in a match.
Return a list answer of size 2 where:
  answer[0] is a list of all players that have not lost any matches.
  answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.
Note:
  You should only consider the players that have played at least one match.
  The testcases will be generated such that no two matches will have the same outcome.
Constraints:
  1 <= matches.length <= 10^5
  matches[i].length == 2
  1 <= winner_i, loser_i <= 10*5
  winner_i != loser_i
  All matches[i] are unique.
"""

from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set(); loosers = defaultdict(int)
        for m in matches:
            winners.add(m[0])
            loosers[m[1]] += 1
        winners_all = [w for w in winners if w not in loosers]
        winners_all.sort()
        loosers_1 = [l for l, cnt in loosers.items() if cnt == 1]
        loosers_1.sort()
        return [winners_all, loosers_1]


sln = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(sln.findWinners(matches))

sln = Solution()
matches = [[2,3],[1,3],[5,4],[6,4]]
print(sln.findWinners(matches))