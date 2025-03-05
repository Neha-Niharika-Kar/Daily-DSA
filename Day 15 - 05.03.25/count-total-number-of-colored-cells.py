# MATHEMATICAL - Medium

# There exists an infinitely large two-dimensional grid of uncolored unit cells. 
# You are given a positive integer n, indicating that you must do the following routine for n minutes:
# At the first minute, color any arbitrary unit cell blue.
# Every minute thereafter, color blue every uncolored cell that touches a blue cell.

# Return the number of colored cells at the end of n minutes.

class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        sum = 0
        for i in range(1,n):
            sum += i
        return 1 + 4*sum
