# ARRAYS - Medium

# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current, total):
            if total == target:
                result.append(list(current))
                return
            
            if i == len(candidates) or total > target:
                return
        
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()

            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  
        result = []

        def backtrack(start, remain, path):
            if remain == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remain:
                    break

                path.append(num)
                backtrack(i, remain - num, path) 
                path.pop()  

        backtrack(0, target, [])
        return result
