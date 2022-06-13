# ARRAYS - Medium

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n,
# a, b, c, and d are distinct, and
# nums[a] + nums[b] + nums[c] + nums[d] == target

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if not nums:
                return res
            avg = target // k
            if avg < nums[0] or avg > nums[-1]:
                return res    
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                add = nums[lo] + nums[hi]
                if add < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif add > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1                                  
            return res

        return kSum(nums, target, 4)
