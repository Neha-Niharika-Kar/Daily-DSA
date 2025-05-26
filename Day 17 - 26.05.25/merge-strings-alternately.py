# STRINGS - Easy

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merge = ""
        while i in range(len(word1)) and j in range(len(word2)):
            merge += word1[i]
            merge += word2[j]
            i += 1
            j += 1
        
        if i < len(word1):
            merge += word1[i:]
        if j < len(word2):
            merge += word2[j:]
        
        return merge
      
