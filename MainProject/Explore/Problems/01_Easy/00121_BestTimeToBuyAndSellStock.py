"""
121. (Easy) Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Constraints:
  1 <= prices.length <= 10^5
  0 <= prices[i] <= 10^4
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0; min_price = float('+inf')
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit

sln = Solution()
print(sln.maxProfit(prices=[7,1,5,3,6,4]))

sln = Solution()
print(sln.maxProfit(prices=[7,6,4,3,1]))