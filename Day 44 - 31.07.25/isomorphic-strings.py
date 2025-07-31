# STRINGS - Easy

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        mapped_chars = set()

        for sc, tc in zip(s, t):
            if sc in map_s_t:
                if map_s_t[sc] != tc:
                    return False
            else:
                if tc in mapped_chars:
                    return False
                map_s_t[sc] = tc
                mapped_chars.add(tc)

        return True
