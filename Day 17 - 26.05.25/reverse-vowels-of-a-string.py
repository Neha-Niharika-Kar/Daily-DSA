# STRINGS - Easy

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ""
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(s)):
            if s[i] in vowels:
                vowel += s[i]
        
        vs = vowel[::-1]
        k = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + vs[k] + s[i+1:]
                k += 1
        return s
