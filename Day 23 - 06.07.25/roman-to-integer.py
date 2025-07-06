# MATHS - Easy

# Given a roman numeral, convert it to an integer.

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

# Special subtractive cases:
IV = 4, IX = 9
XL = 40, XC = 90
CD = 400, CM = 900

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 }

        total = 0
        prev_value = 0

        for c in reversed(s):
            curr_value = roman[c]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value

        return total
