# STRINGS - Easy

# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
# You are given a positive integer k.

# Now Bob will ask Alice to perform the following operation forever:
# Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

class Solution:
    def kthCharacter(self, k: int) -> str:
        def increment_char(char):
            return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        
        word = 'a'
        while len(word) < k:
            incremented = ''.join(increment_char(c) for c in word)
            word += incremented
        return word[k-1]
