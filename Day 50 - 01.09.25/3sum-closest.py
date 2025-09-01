# ARRAYS - Medium

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(closest - target):
                    closest = current
                
                if current == target:
                    return current
                elif current < target:
                    left += 1
                else:
                    right -= 1
        
        return closest
