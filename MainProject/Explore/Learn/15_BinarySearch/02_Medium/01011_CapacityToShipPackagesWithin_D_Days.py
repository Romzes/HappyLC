# Medium 1011. Capacity To Ship Packages Within D Days
# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution:
    def shipWithinDays(self, weights, days):
        pass

sln = Solution()
print(sln.shipWithinDays(weights=[1,2,3,4,5,6,7,8,9,10], days=5))

sln = Solution()
print(sln.shipWithinDays(weights=[3,2,2,4,1,4], days=3))

sln = Solution()
print(sln.shipWithinDays(weights=[1,2,3,1,1], days=4))