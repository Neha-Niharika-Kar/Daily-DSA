# MATHS - Medium

# Given an integer array nums where every element appears three times except for one, which appears exactly once. 
# Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, freq in count.items():
            if freq == 1:
                return num

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):   # loop over 32 bits
            bit_sum = 0
            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1
            
            if bit_sum % 3:
                if i == 31:     # sign bit
                    result -= (1 << i)
                else:
                    result |= (1 << i)
        return result
