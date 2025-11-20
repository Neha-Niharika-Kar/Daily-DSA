# ARRAYS - Medium

# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, remain, path):
            if remain == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                if num > remain:
                    break

                path.append(num)
                backtrack(i + 1, remain - num, path)
                path.pop()

        backtrack(0, target, [])
        return result
