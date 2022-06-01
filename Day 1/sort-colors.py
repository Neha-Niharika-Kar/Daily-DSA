# ARRAYS - Easy

# Given an array 'nums' with n objects colored red, white, or blue.
# Sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(0, len(nums)):    
            for j in range(i+1, len(nums)):    
                if(nums[i] > nums[j]):    
                    nums[i], nums[j] = nums[j], nums[i] 
