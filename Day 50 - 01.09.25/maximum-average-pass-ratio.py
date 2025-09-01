# ARRAYS - Medium

# There is a school that has classes of students and each class will be having a final exam. 
# You are given a 2D integer array classes, where classes[i] = [passi, totali]. 
# You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. 
# You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. 
# The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (t - p) / (t * (t + 1))
        
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t
        return total / len(classes)
 
