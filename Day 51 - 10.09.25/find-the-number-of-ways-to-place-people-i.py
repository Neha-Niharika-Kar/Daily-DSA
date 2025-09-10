# ARRAYS - Medium

# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].
# Count the number of pairs of points (A, B), where
# A is on the upper left side of B, and
# there are no other points in the rectangle (or line) they make (including the border).
# Return the count.

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        
        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 <= x2 and y1 >= y2 and (x1 < x2 or y1 > y2):
                    valid = True
                    for k in range(n):
                        if k == i or k == j: 
                            continue
                        xk, yk = points[k]
                        if x1 <= xk <= x2 and y2 <= yk <= y1:
                            valid = False
                            break
                    if valid:
                        ans += 1
        
        return ans
