# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer has in the j-th bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts):
        mw = float('-inf')
        for client in accounts: mw = max(mw, sum(client))
        return mw

class Solution:
    def maximumWealth(self, accounts):
        return max(sum(client) for client in accounts)

sln = Solution()
accounts = [[1,2,3],[3,2,1]]
print(sln.maximumWealth(accounts))

sln = Solution()
accounts = [[1,5],[7,3],[3,5]]
print(sln.maximumWealth(accounts))

sln = Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(sln.maximumWealth(accounts))