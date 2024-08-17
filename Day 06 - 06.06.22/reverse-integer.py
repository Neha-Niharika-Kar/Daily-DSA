# MATHEMATICAL - Easy

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range, then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0: 
            a =  int(str(x)[::-1])  
        if x <= 0:  
            a = -1 * int(str(x*-1)[::-1])  
        mini = -2**31  
        maxi = 2**31 - 1  
        if a not in range(mini, maxi):  
            return 0  
        else:  
            return a
