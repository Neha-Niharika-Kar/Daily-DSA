# MATH - Medium

# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
# Return true if and only if we can do this so that the resulting number is a power of two.

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_set = {tuple(sorted(str(1 << i))) for i in range(31)}
        return tuple(sorted(str(n))) in power_set
