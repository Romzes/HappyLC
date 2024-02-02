"""
1291 (Medium) Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
Constraints: 10 <= low <= high <= 10^9
"""
from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        low_str = str(low); lng1 = len(low_str)
        res.extend(self.gen(lng1, low, high, int(low_str[0])))
        lng2 = len(str(high))
        for lng in range(lng1+1, lng2+1): res.extend(self.gen(lng, low, high))
        return res

    def gen(self, lng, low, high, start_digit=1):
        arr = []
        for d in range(start_digit, 10 - lng + 1):
            m = 0
            for v in range(d, d+lng): m = 10*m + v
            if m < low: continue
            if m > high: break
            arr.append(m)
        return arr

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        templ = '123456789'
        res = []
        lng1 = len(str(low)); lng2 = len(str(high))
        for lng in range(lng1, lng2+1):
            for i in range(10-lng):
                v = int(templ[i:i+lng])
                if low <= v <= high: res.append(v)
        return res

sln = Solution()
print(sln.sequentialDigits(low=100, high=300))

sln = Solution()
print(sln.sequentialDigits(low=1000, high=13000))