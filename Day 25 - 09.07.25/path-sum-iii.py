# TREES - Medium

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, psum):
            if not node:
                return 0
            
            psum += node.val
            count = prefix[psum - targetSum] 
            prefix[psum] += 1
            
            count += dfs(node.left, psum)
            count += dfs(node.right, psum)

            prefix[psum] -= 1
            return count
        
        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)
