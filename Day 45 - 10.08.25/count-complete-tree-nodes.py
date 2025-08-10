# TREES - Easy

# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, 
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def rightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        if not root:
            return 0
        
        lh = leftHeight(root)
        rh = rightHeight(root)

        if lh == rh:  
            return (1 << lh) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
