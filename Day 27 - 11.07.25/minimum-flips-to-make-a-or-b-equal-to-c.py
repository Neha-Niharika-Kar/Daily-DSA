# BITS - Medium

# Given 3 positives numbers a, b and c. 
# Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if (a_bit | b_bit) != c_bit:
                if c_bit == 1:
                    flips += 1  
                else:
                    flips += a_bit + b_bit
            a >>= 1
            b >>= 1
            c >>= 1

        return flips 
