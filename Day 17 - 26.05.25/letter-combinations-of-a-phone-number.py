# ARRAYS - Medium

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        key = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        
        result = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return
            possible_letters = key[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result
