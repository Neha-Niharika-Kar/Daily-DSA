# STRINGS - Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if open brackets must be closed by the same type of brackets, and open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in range(len(s)):
            if(s[i]=='{'or s[i]=="[" or s[i]=="("):
                l.append(s[i])
            elif(len(l)!=0 and l[-1]=="(" and s[i]==")"):
                l.pop()
            elif(len(l)!=0 and l[-1]=="[" and s[i]=="]"):
                l.pop()
            elif(len(l)!=0 and l[-1]=="{" and s[i]=="}"):
                l.pop()
            else:
                return False
        if(len(l) == 0):
            return True
        else:
            return False
