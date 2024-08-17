# ARRAYS - Medium

# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        current_score = sum(cardPoints[:k])
        max_score = current_score
        
        for i in range(1, k + 1):
            current_score += cardPoints[-i] - cardPoints[k - i]
            max_score = max(max_score, current_score)
        
        return max_score
