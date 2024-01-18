"""
1436 (Easy) Destination City
You are given the array paths, where paths[i] = [cityA_i, cityB_i] means there exists a direct path going from cityA_i to cityB_i.
Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
Constraints:
  1 <= paths.length <= 100
  paths[i].length == 2
  1 <= cityA_i.length, cityB_i.length <= 10
  cityA_i != cityB_i
  All strings consist of lowercase and uppercase English letters and the space character.
"""

from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set(p[0] for p in paths)
        for p in paths:
            if p[1] not in src: return p[1]

sln = Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(sln.destCity(paths))

sln = Solution()
paths = [["B","C"],["D","B"],["C","A"]]
print(sln.destCity(paths))

sln = Solution()
paths = [["A","Z"]]
print(sln.destCity(paths))