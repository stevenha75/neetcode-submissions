# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bottom up + dfs approach 
        # left = right, right = left? 

        # when doing recursion u need a base case
        def dfs(node):
            if not node:
                return None
                # not sure what it returns up?

            dfs(node.left)
            dfs(node.right)

            # flip
            node.left, node.right = node.right, node.left
            return node

        return dfs(root)


        