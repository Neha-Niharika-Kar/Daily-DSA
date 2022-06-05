# SORTING AND SEARCHING - Easy

# Given an array arr[] of size L and a number N, find if there exists a pair of elements in the array whose difference is N. 

class Solution:
    def findPair(self, arr, L, N):
        arr.sort()
        i,j = 0,1
        while i < L and j < L:
            if i != j and arr[j] - arr[i] == N:
                return 1
            elif arr[j] - arr[i] > N:
                i += 1
            else:
                j += 1
        return -1
