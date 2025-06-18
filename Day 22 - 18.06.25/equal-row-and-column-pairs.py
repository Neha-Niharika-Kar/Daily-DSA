# ARRAY - Medium

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        for r in range(n):  
            for c in range(n):  
                match = True
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = False
                        break
                if match:
                    count += 1
                    
        return count
