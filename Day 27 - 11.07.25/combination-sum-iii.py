# BACKTRACKING - Medium

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. 
# The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []
        result = []
        
        def backtrack(start, path, target):
            if len(path) == k:
                if target == 0:
                    result.append(path[:])
                return
            
            for i in range(start, 10):
                if i > target:
                    break
                path.append(i)
                backtrack(i+1, path, target-i)
                path.pop()
            
        backtrack(1, [], n)
        return result
