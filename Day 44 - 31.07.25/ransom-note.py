# STRINGS - Easy

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = {}

        for char in magazine:
            letter_count[char] = letter_count.get(char, 0) + 1

        for char in ransomNote:
            if char not in letter_count or letter_count[char] == 0:
                return False
            letter_count[char] -= 1

        return True


from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char in ransomNote:
            if ransom_count[char] > magazine_count.get(char, 0):
                return False
        return True
