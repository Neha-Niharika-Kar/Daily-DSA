# ARRAYS - Easy

# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array. If there is no lucky integer return -1.

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        lucky = []
        for i in count.keys():
            if i == count[i]:
                lucky.append(i)
        
        if not lucky:
            return -1
        return max(lucky)
