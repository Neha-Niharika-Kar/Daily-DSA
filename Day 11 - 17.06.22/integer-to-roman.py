# STRINGS - Medium

# Given an integer, convert it to a roman numeral.

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
#   I            1
#   V            5
#   X            10
#   L            50
#   C            100
#   D            500
#   M            1000

# Roman numerals are usually written largest to smallest from left to right. 

# There are six instances where subtraction is used:
# 1. I can be placed before V (5) and X (10) to make 4 and 9. 
# 2. X can be placed before L (50) and C (100) to make 40 and 90. 
# 3. C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        numerals = { "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                    "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1 }
        for symbol, value in numerals.items():
            roman += (num // value) * symbol
            num %= value
        return roman
