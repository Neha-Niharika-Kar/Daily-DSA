# ARRAYS - Easy

# Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. 
# Each packet can have a variable number of chocolates. 

# There are M students, the task is to distribute chocolate packets among M students such that :
# 1. Each student gets exactly one packet.
# 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

class Solution:
    def findMinDiff(self, A, N, M):
        A.sort()
        if (M==0 or N==0):
            return 0
        if (N < M):
            return -1
        diff = A[N-1] - A[0]
        for i in range(len(A) - M + 1):
            diff = min(diff,  A[i+M-1] - A[i])
        return diff
