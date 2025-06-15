# ARRAYS - Medium

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. 
# In this process, births and deaths occur simultaneously.
# Given the current state of the board, update the board to reflect its next state.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
    
        def countLiveNeighbors(r, c):
            live_neighbors = 0
            for i in range(max(0, r - 1), min(rows, r + 2)):
                for j in range(max(0, c - 1), min(cols, c + 2)):
                    if (i, j) != (r, c) and abs(board[i][j]) == 1:
                        live_neighbors += 1
            return live_neighbors
            
        for r in range(rows):
            for c in range(cols):
                live_neighbors = countLiveNeighbors(r, c)
                
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1  # Alive → Dead
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2   # Dead → Alive

        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
