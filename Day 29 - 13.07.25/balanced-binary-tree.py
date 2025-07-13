# TREES - Easy

# Given a binary tree, determine if it is height-balanced.
# A binary tree in which the left and right subtrees of every node differ in height by no more than 1 is called height-balanced.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            if left == -1:
                return -1

            right = check(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return check(root) != -1
