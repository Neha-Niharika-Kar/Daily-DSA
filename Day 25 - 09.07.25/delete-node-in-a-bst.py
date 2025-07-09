# TREES - Medium

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
# Return the root node reference (possibly updated) of the BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            if node.left is None:
                return node.val
            return find_min(node.left)
        
        def delete(node, val):
            if not node:
                return None
            
            if val < node.val:
                if node.left:
                    node.left = delete(node.left, val)

            elif val > node.val:
                if node.right:
                    node.right = delete(node.right, val)
            
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                min_val = find_min(node.right)
                node.val = min_val
                node.right = delete(node.right, min_val)
            
            return node
        
        return delete(root,key)
