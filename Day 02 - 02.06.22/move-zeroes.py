# ARRAYS - Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeros] = nums[i]
                zeros += 1
        while zeros < len(nums):
            nums[zeros] = 0
            zeros += 1
