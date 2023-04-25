# Medium 322. Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

### Recursive
class Solution:
    def coinChange(self, coins, amount):
        self.memo = {}
        self.coins = coins
        self.coins.sort()
        return self.calc_coin_cnt(amount)

    def calc_coin_cnt(self, amount):
        if amount == 0: return 0
        coin_cnt = self.memo.get(amount)
        if coin_cnt is not None: return coin_cnt
        numbers = []
        for cn in self.coins:
            rest = amount - cn
            if rest < 0: break
            coin_cnt = 0 if rest == 0 else self.calc_coin_cnt(amount=rest)
            if coin_cnt != -1: numbers.append(coin_cnt)
        coin_cnt = self.memo[amount] = 1 + min(numbers) if numbers else -1
        return coin_cnt

### Iterative
class Solution:
    def coinChange(self, coins, amount):
        memo = (amount+1)*[float('inf')]; memo[0] = 0
        for a in range(1, amount+1):
            for cn in coins:
                r = a - cn
                if r >= 0: memo[a] = min(memo[a], 1+memo[r])
        return memo[-1] if memo[-1] != float('inf') else -1


sln = Solution()
print(sln.coinChange(coins=[1,2,5], amount=11))

sln = Solution()
print(sln.coinChange(coins=[2], amount=3))