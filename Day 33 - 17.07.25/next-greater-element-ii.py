# STACKS - Medium

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, 
# which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  

        for i in range(2 * n):
            curr_index = i % n
            while stack and nums[curr_index] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[curr_index]
            if i < n:  
                stack.append(curr_index)

        return result 
