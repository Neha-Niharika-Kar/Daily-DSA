# ARRAYS - Medium

# Given a string s, return the longest palindromic substring in s.

# Brute Force - O(n3)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1]
                if substr == substr[::-1] and len(substr) > len(res):
                    res = substr
        return res

# Expand Around Center - O(n2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # substring after mismatch

        res = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i, i)      # Odd length palindrome
            even = expandAroundCenter(i, i + 1)     # Even length palindrome

            longer = odd if len(odd) > len(even) else even
            if len(longer) > len(res):
                res = longer
        
        return res


# Manacher's Algorithm - O(n)
