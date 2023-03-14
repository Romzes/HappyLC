# Medium 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# исходный grid не меняется
class Solution:
    def numIslands(self, grid):
        # grid: List[List[str]], return int
        self.grid, self.M, self.N = grid, len(grid), len(grid[0])
        self.islands, self.planned = 0, set()
        for i in range(self.M):
            for j in range(self.N):
                self.build_island(i, j)
        return self.islands

    def build_island(self, i, j):
        if self.grid[i][j] == '0': return
        root = (i, j)
        if root in self.planned: return
        self.planned.add(root)
        stack = [(i, j)]
        while len(stack) > 0:
            cell = stack.pop()
            for neigh_cell in self.get_neigh_cells(cell):
                if neigh_cell not in self.planned:
                    self.planned.add(neigh_cell)
                    stack.append(neigh_cell)
        self.islands += 1

    def get_neigh_cells(self, cell):
        neigh_cells = []
        i, j = cell
        for i1, j1 in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if 0 <= i1 < self.M and 0 <= j1 < self.N and self.grid[i1][j1] == '1': neigh_cells.append((i1, j1))
        return neigh_cells

# исходный grid меняется
class Solution:
    def numIslands(self, grid):
        # grid: List[List[str]], return int
        self.grid, self.M, self.N = grid, len(grid), len(grid[0])
        self.islands = 0
        for i in range(self.M):
            for j in range(self.N):
                if self.grid[i][j] == '0': continue
                self.build_island(i, j)
        return self.islands

    def build_island(self, i, j):
        stack = [(i, j)]
        while len(stack) > 0:
            cell = stack.pop()
            self.grid[cell[0]][cell[1]] = '0'
            for neigh_cell in self.get_neigh_1cells(cell): stack.append(neigh_cell)
        self.islands += 1

    def get_neigh_1cells(self, cell):
        neigh_cells = []
        i, j = cell
        for i1, j1 in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if 0 <= i1 < self.M and 0 <= j1 < self.N and self.grid[i1][j1] == '1': neigh_cells.append((i1, j1))
        return neigh_cells

########## TEST ########################################################################################################
sln = Solution()
grid = [
    ['0', '1', '0', '1'],
    ['1', '0', '1', '1'],
    ['0', '0', '0', '1'],
]
print(sln.numIslands(grid))

sln = Solution()
grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]
print(sln.numIslands(grid))