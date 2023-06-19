# Medium 735. Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.
# Constraints:
#   2 <= asteroids.length <= 104
#   -1000 <= asteroids[i] <= 1000
#   asteroids[i] != 0

class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for a in asteroids:
            if a > 0:
                res.append(a)
                continue
            # a < 0
            while True:
                if not res or res[-1] < 0:
                    res.append(a)
                    break
                r = res[-1]; pa = abs(a)
                if r >= pa:
                    if r == pa: res.pop()
                    break
                res.pop()
        return res

sln = Solution()
print(sln.asteroidCollision(asteroids=[5,10,-5]))

sln = Solution()
print(sln.asteroidCollision(asteroids=[8,-8]))

sln = Solution()
print(sln.asteroidCollision(asteroids=[10,2,-5]))