# STRINGS - Easy

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. 
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string = s.split()
        if len(pattern) != len(string):
            return False
            
        smap = {}
        mapped = set()

        for pc, sc in zip(pattern, string):
            if pc in smap:
                if smap[pc] != sc:
                    return False
            else:
                if sc in mapped:
                    return False
                smap[pc] = sc
                mapped.add(sc)

        return True
