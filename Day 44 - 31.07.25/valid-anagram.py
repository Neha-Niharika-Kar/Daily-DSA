# STRINGS - Easy

# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# An anagram means the same letters with the same frequency, but possibly in a different order.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = Counter(s)
        tcount = Counter(t)
        return scount == tcount


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        return True
