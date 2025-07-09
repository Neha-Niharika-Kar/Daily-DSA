# TREES - Medium

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        
        sums = []
        queue = deque([root])

        while queue:
            levelsize = len(queue)
            levelsum = 0

            for _ in range(levelsize):
                node = queue.popleft()
                levelsum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            sums.append(levelsum)
        
        return sums.index(max(sums)) + 1
