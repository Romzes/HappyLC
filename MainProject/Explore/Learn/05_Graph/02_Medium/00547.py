# Medium 547. Number of Provinces
# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

class Solution:
    def findCircleNum(self, isConnected):
        root = [i for i in range(len(isConnected))]
        for i, row in enumerate(isConnected):
            for j in row:
                if j == i: continue
                root[j] = root[i]