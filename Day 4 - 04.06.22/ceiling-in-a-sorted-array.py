# SORTING AND SEARCHING - Easy

# Given a sorted array and a value x, find the ceiling of x.
# Assume that the array is sorted in non-decreasing order. 

class Solution:
    def findCeil(self, arr, low, high, x):
        if x > arr[high]:
            return -1
        if x <= arr[low]:
            return low
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            if mid - 1 >= low and x > arr[mid-1]:
                return mid
            else:
                return findCeil(arr, low, mid - 1, x)
        else:
            if mid + 1 <= high and x <= arr[mid+1]:
                return mid + 1
            else:
                return findCeil(arr, mid + 1, high, x)
