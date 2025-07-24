# MATRIX - Medium

# Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). 
# Find the number of islands.

# An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands 
# horizontally or vertically or diagonally i.e., in all 8 directions.

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 'L':
                return
            grid[r][c] = 'V' 
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':
                    count += 1
                    dfs(r, c)

        return count
