# STRINGS - Medium

# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char and char[s[right]] >= left:
                left = char[s[right]] + 1
            
            char[s[right]] = right
            max_len = max(max_len, right - left + 1)
                
        return max_len
