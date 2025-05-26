# ARRAYS - Medium

# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0

        def expand_around_center(left: int, right: int):
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            if right - left - 1 > end - start:
                start = left + 1
                end = right - 1
        
        for i in range(len(s)):
            expand_around_center(i,i)
            expand_around_center(i,i+1)
        
        return s[start:end+1]
      
