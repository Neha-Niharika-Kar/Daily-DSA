# ARRAYS - Medium

# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        add = 0
        sub = 0
        for i in range(len(nums)):
            add += nums[i]
            rem = add % k
            if rem < 0:
                rem += k
            if rem in d:
                sub += d[rem]
                d[rem] += 1
            else:
                d[rem] = 1
        return sub
