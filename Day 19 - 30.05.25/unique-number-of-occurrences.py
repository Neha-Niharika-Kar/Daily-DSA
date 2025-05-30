# ARRAYS - Easy

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = []
        arr1 = list(set(arr))
        for a in arr1:
            count = arr.count(a)
            occur.append(count)
        
        return len(occur) == len(set(occur))
