# STACKS AND QUEUES - Easy

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string):
            result = []
            for char in string:
                if char == '#':
                    if result: 
                        result.pop()
                else:
                    result.append(char)
            return result
        return processString(s) == processString(t)
