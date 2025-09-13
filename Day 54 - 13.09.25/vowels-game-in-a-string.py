# STRINGS - Medium

# Alice and Bob are playing a game on a string.
# You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:
# On Alice's turn, she has to remove any non-empty substring from s that contains an odd number of vowels.
# On Bob's turn, he has to remove any non-empty substring from s that contains an even number of vowels.

# The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.
# Return true if Alice wins the game, and false otherwise.

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        for ch in s:
            if ch in vowels:
                return True
        return False

# If k = 0 (no vowels): Alice loses immediately (because she cannot make a move), so Bob wins. 
# If k >= 1 Alice always wins.

# If k is odd: Alice can remove the entire string in her first move (since the whole string has odd number of vowels), 
# and Bob has no move then. Alice wins. 

# If k is even (and ≥ 2): Alice can remove a substring that contains k - 1 vowels (which is odd), 
# leaving exactly 1 vowel in the (remaining) string. Then it's Bob’s turn. 
# Bob must remove a substring with an even number of vowels; but the remaining string has 1 vowel (odd), so Bob cannot. 
# Bob loses. Alice wins.
