# ARRAYS - Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    sol.add((nums[i], nums[j], nums[k]))
                if nums[i] + nums[j] + nums[k] <= 0:  
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
        return list(map(list, sol))
