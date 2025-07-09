# STRINGS - Medium

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')
        vowels = 0
        for i in range(k):
            if s[i] in vowel:
                vowels += 1
        max_vowels = vowels

        for i in range(k, len(s)):
            if s[i] in vowel:
                vowels += 1
            if s[i-k] in vowel:
                vowels -= 1
            max_vowels = max(max_vowels, vowels)
        
        return max_vowels
