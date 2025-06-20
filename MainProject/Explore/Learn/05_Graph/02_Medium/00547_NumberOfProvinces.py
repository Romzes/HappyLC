# Medium 547. Number of Provinces
# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the i-th city and the j-th city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Runtime = 3 ms  Beats 89.39%  ;  Memory = 19.06 MB  Beats 57.19%
class Solution:
    def findCircleNum(self, isConnected):
        self.isConnected = isConnected
        self.cities = len(isConnected) * [-1]  # необработанные города помечены = -1
        prov = 0
        for c0 in range(len(isConnected)):
            if self.cities[c0] != -1: continue
            self.find_province(c0, prov)
            prov += 1
        return prov

    def find_province(self, c0, prov):
        # все города, лежащие в одной провинции вместе с городом-c0, получат номер провинции = prov
        # self.cities[c0-провинция] = prov
        stack = [c0]
        while stack:
            c1 = stack.pop()
            if self.cities[c1] != -1: continue  # город-c1 уже принадлежит некоторой провинции prov
            self.cities[c1] = prov
            for c2, flag in enumerate(self.isConnected[c1]):
                if flag == 0 or self.cities[c2] != -1: continue
                stack.append(c2)


sln = Solution()
isConnected=[[1,1,0],[1,1,0],[0,0,1]]
print(sln.findCircleNum(isConnected))  # Output: 2

sln = Solution()
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(sln.findCircleNum(isConnected))  # Output: 3