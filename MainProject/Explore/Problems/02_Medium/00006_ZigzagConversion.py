# 6 (Medium) Zigzag Conversion
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

Constraints:
  1 <= s.length <= 1000
  s consists of English letters (lower-case and upper-case), ',' and '.'.
  1 <= numRows <= 1000
"""

# Runtime = 9 ms  Beats 72.60%  ;  Memory = 17.99 MB  Beats 50.89%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [[] for _ in range(numRows)]
        r, dr = 0, 1
        for c in s:
            rows[r].append(c)
            if r == 0: dr = 1
            if r == numRows-1: dr = -1
            r += dr
        return ''.join(''.join(row) for row in rows)


sln = Solution()
print(sln.convert(s='PAYPALISHIRING', numRows=3))  # Output: 'PAHNAPLSIIGYIR'

sln = Solution()
print(sln.convert(s='PAYPALISHIRING', numRows=4))  # Output: 'PINALSIGYAHRPI'

sln = Solution()
print(sln.convert(s='A', numRows=1))  # Output: 'A'