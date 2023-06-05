# Easy 1232. Check If It Is a Straight Line
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
# Constraints:
#   2 <= coordinates.length <= 1000
#   coordinates[i].length == 2
#   -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#   coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates):
        n = len(coordinates)
        if n <= 2: return True
        a,b,c = self.calc_line(x1=coordinates[0][0], y1=coordinates[0][1], x2=coordinates[1][0], y2=coordinates[1][1])
        for i in range(2, n):
            if a*coordinates[i][0] + b*coordinates[i][1] != c: return False
        return True

    def calc_line(self, x1, y1, x2, y2):
        if x1 != x2:
            a = (y2-y1)/(x2-x1); b = -1; c = a*x1 - y1
        else:
            a = 1; b = 0; c = x1
        return a,b,c  # line equation : a*x + b*y = c


sln = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(sln.checkStraightLine(coordinates))

sln = Solution()
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(sln.checkStraightLine(coordinates))
