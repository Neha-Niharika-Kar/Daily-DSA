# DP - Medium

# Given an integer array nums, find a subarray that has the largest product, and return the product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_prod = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, num * curr_max)
            curr_min = min(num, num * curr_min)
            max_prod = max(max_prod, curr_max)

        return max_prod
