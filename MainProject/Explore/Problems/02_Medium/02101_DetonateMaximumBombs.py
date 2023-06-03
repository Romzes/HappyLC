# Medium 2101. Detonate the Maximum Bombs
# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt.
# This area is in the shape of a circle with the center as the location of the bomb.
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
# xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range.
# These bombs will further detonate the bombs that lie in their ranges.
# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

class Solution:
    def maximumDetonation(self, bombs):
        # bombs: List[List[int]]
        self.graph = self.create_graph(bombs)
        all_visited = set(); mx = 0
        for i0 in range(len(bombs)):
            if i0 in all_visited: continue
            detonated = self.detonate(i0)
            mx = max(mx, len(detonated))
            all_visited.update(detonated)
        return mx

    def detonate(self, i0):
        stack = [i0]; detonated = set(stack)
        while stack:
            i1 = stack.pop()
            for i2 in self.graph[i1]:
                if i2 in detonated: continue
                stack.append(i2)
                detonated.add(i2)
        return detonated

    def create_graph(self, bombs):
        graph = [[] for _ in range(len(bombs))]
        for i, b1 in enumerate(bombs):
            r2 = b1[2]**2
            for j, b2 in enumerate(bombs):
                if i == j: continue
                if (b2[0] - b1[0])**2 + (b2[1] - b1[1])**2 <= r2: graph[i].append(j)
        return graph

sln = Solution()
bombs = [[2,1,3],[6,1,4]]
print(sln.maximumDetonation(bombs))

sln = Solution()
bombs = [[1,1,5],[10,10,5]]
print(sln.maximumDetonation(bombs))

sln = Solution()
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
print(sln.maximumDetonation(bombs))