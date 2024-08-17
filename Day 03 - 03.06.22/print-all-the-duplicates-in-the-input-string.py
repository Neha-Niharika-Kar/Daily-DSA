# STRINGS - Easy

# Given a string s, print all the duplicates and their counts in the string.

class Solution:
    def printDups(s):
        char = {}
        for i in range(len(s)):
            if s[i] in char:
                char[s[i]] += 1
            else:
                char[s[i]] = 1
        for ch,i in char.items():  
            if i > 1:  
                print(ch, i)
