# STACKS - Medium

# Given an array of integers temperatures represents the daily temperatures, return an array answer 
# such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        answer = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        
        return answer
