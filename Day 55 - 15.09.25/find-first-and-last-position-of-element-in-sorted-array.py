# ARRAYS - Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        positions = []
        for i, val in enumerate(nums):
            if val == target:
                positions.append(i)
        
        if not positions:
            return [-1, -1]
        
        return [positions[0], positions[-1]]
      
