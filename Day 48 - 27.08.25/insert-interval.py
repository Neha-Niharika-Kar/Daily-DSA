# ARRAYS - Medium

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last = merged[-1][1]

            if start <= last:
                merged[-1][1] = max(last, end)
            else:
                merged.append([start, end])

        return merged
