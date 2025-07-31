# STRINGS - Medium

# Given an array of strings, group the anagrams together. You can return the answer in any order.
# Anagrams are words that contain the same characters in a different order (same frequency of each letter).

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())
