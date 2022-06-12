# ARRAYS - Medium

# Given an integer array nums of length n, where all the integers of nums are in the range [1, n] and each integer appears once or twice.
# Return an array of all the integers that appears twice.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup.append(nums[i-1])
        return dup
