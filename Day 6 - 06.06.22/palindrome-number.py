# MATHEMATICAL - Easy

# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
        if num == rev:
            return True
        else:
            return False
