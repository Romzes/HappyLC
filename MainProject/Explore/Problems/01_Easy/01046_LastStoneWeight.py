# Easy 1046. Last Stone Weight
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#   If x == y, both stones are destroyed, and
#   If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

import heapq

class Solution:
    def lastStoneWeight(self, stones):
        for i in range(len(stones)): stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) >= 2:
            d = heapq.heappop(stones) - heapq.heappop(stones)
            if d != 0: heapq.heappush(stones, d)
        return 0 if len(stones) == 0 else -stones[0]

sln = Solution()
print(sln.lastStoneWeight(stones=[2,7,4,1,8,1]))

sln = Solution()
print(sln.lastStoneWeight(stones=[1]))
