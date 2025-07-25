# HEAP - Medium

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        heapq.heapify(minheap)
        for i in range(k, len(nums)):
            if nums[i] > minheap[0]:
                heapq.heappushpop(minheap, nums[i])
        return minheap[0]
