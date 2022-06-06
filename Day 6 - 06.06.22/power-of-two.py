# MATHEMATICAL - Easy

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and log2(n) == trunc(log2(n))
