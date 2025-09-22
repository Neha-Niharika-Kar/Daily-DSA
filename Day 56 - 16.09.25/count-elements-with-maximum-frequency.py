# ARRAYS - Easy

# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        total_freq = 0

        for num in count:
            if count[num] == max_freq:
                total_freq += count[num]
        
        return total_freq
