# ARRAYS - Medium

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub = 0
        add = 0
        d = {0:1}
        for num in nums:
            add += num
            if add-k in d:
                sub = sub + d[add-k]
            d[add] = d.get(add, 0) + 1
        return sub
