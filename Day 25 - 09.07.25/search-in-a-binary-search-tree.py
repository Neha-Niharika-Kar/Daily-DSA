# TREES - Easy

# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def in_order(node):
            elements = []
            if node is None:
                return None 
           
            if node.left:
                elements += in_order(node.left)
            
            elements.append(node.val)

            if node.right:
                elements += in_order(node.right)
            
            return elements

        def search(node, val):
            if node is None:
                return None

            if node.val == val:
                return node
            
            if val < node.val:
                if node.left:
                    return search(node.left, val)
            
            if val > node.val:
                if node.right:
                    return search(node.right, val)

        node = search(root, val)
        print(in_order(node))
        return node
