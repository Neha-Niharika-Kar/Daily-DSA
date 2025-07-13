# TREES - Easy

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, res):
            if not node:
                return
        
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            
            else:
                path += "->"
                dfs(node.left, path, res)
                dfs(node.right, path, res)

        result = []
        dfs(root, "", result)
        return result
