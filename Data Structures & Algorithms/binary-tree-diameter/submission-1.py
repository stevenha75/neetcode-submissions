# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # finds the longest path
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0 # there is a height of 0 from this node
            
            # signifying we want to use the res var declared outside of this scope
            nonlocal res

            # calculating the heights of the left, right side
            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res, left + right) # diameter from node is left + right

            # returning max height from this current node
            return 1 + max(left, right)

        dfs(root)
        return res
 