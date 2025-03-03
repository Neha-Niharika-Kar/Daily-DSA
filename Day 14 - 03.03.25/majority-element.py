# ARRAYS - Medium

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count.keys(), key=count.get)
