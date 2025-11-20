# MATH - Medium

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            result += multiple
        
        return -result if negative else result
