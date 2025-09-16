# STACKS - Hard

# You are given an array of integers nums. Perform the following steps:
# Find any two adjacent numbers in nums that are non-coprime.
# If no such numbers are found, stop the process.
# Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
# Repeat this process as long as you keep finding two adjacent non-coprime numbers.
# Return the final modified array.

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for x in nums:
            stack.append(x)
        
            while len(stack) >= 2:
                a = stack[-2]
                b = stack[-1]
                g = gcd(a, b)
                if g == 1:
                    break
        
                stack.pop()
                l = (a // g) * b
                stack[-1] = l

        return stack
