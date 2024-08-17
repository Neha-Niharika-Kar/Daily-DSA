# SORTING AND SEARCHING - Easy

# Given a sorted array and a value x, find the floor of x.
# Assume that the array is sorted in non-decreasing order. 

class Solution:
    def findFloor(self, A, N, x):
        l, h = 0, N-1
        if (l > h):
            return -1
        if (x >= A[h]):
            return h
        while l <= h:
            mid = (l+h)//2
            if A[mid] == x:
                return mid
            elif A[mid] > x:
                h = mid-1
            else:
                if A[h] <= x:
                    return h
                else:
                    h-=1
        return -1
