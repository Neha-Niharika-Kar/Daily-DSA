# BITS - Easy

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            binary = bin(i)
            ones = binary.count('1')
            ans.append(ones)
        return ans
