# HEAP - Medium

# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.added_back = set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added_back.remove(smallest)
            return smallest
        else:
            val = self.curr
            self.curr += 1
            return val

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.added_back:
            heapq.heappush(self.heap, num)
            self.added_back.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
