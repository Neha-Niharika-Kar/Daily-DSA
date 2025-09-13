# STRINGS - Easy

# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. 
# If there are no vowels or no consonants in the string, consider their frequency as 0.

from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        vowels = 'aeiou'
        v_freq, c_freq = [], []

        for value in count:
            if value in vowels:
                v_freq.append(count[value])
            else:
                c_freq.append(count[value])
        
        v_max = max(v_freq) if v_freq else 0
        c_max = max(c_freq) if c_freq else 0

        return v_max + c_max
