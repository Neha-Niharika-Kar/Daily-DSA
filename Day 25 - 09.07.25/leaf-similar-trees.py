# TREES - Easy

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find_leaf_nodes(root, leaf):
            if root is None:
                return
            
            if root.left is None and root.right is None:
                leaf.append(root.val)
            else:
                find_leaf_nodes(root.left, leaf)
                find_leaf_nodes(root.right, leaf)

            return leaf
        
        leaf1 = []
        find_leaf_nodes(root1, leaf1)
        leaf2 = []
        find_leaf_nodes(root2, leaf2)

        return leaf1 == leaf2
