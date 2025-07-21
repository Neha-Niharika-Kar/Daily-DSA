# DP - Easy

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [1]  

            if triangle: 
                last_row = triangle[-1]
                for i in range(1, row_num):
                    row.append(last_row[i-1] + last_row[i])
                row.append(1) 

            triangle.append(row)

        return triangle
