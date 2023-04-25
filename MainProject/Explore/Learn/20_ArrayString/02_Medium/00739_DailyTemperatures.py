# Medium 739. Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

### Memory NOT optimized
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures); res = n*[0]
        if n <= 1: return res
        stack = [0]
        for i in range(1, n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack[-1]; res[j] = i - j
                stack.pop()
            stack.append(i)
        return res

sln = Solution()
print(sln.dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73]))

sln = Solution()
print(sln.dailyTemperatures(temperatures=[30,40,50,60]))

sln = Solution()
print(sln.dailyTemperatures(temperatures=[30,60,90]))