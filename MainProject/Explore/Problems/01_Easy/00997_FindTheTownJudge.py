"""
997 (Easy) Find the Town Judge
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
  The town judge trusts nobody.
  Everybody (except for the town judge) trusts the town judge.
  There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [a_i, b_i] representing that the person labeled a_i trusts the person labeled b_i.
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
Constraints:
  1 <= n <= 1000
  0 <= trust.length <= 10^4
  trust[i].length == 2
  All the pairs of trust are unique.
  a_i != b_i
  1 <= a_i, b_i <= n
"""
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        towns = (n+1)*[0]  # для города k: towns[k] = (входящие - исходящие)
        m = n-1; res = []
        for a, b in trust:
            towns[a] = None
            if towns[b] is not None:
                towns[b] += 1
                if towns[b] == m: res.append(b)
        for b in res:
            if towns[b] is not None: return b
        return -1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        towns = (n+1)*[0]  # для города k: towns[k] = (входящие - исходящие)
        for a, b in trust:
            towns[a] -= 1
            towns[b] += 1
        try:
            return towns.index(n-1)
        except:
            return -1

sln = Solution()
print(sln.findJudge(n=2, trust=[[1,2]]))

sln = Solution()
print(sln.findJudge(n=3, trust=[[1,3],[2,3]]))

sln = Solution()
print(sln.findJudge(n=3, trust=[[1,3],[2,3],[3,1]]))