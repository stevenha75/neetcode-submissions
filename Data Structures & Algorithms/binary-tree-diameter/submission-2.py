# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # bruteforce
    # o(n) time, o(n) space
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mdia = 0

        def dfs(node):
            nonlocal mdia

            if not node:
                return 0 

            # diameter is height of left + right
            lefth = dfs(node.left)
            righth = dfs(node.right)
            mdia = max(mdia, lefth + righth)
            
            return 1 + max(dfs(node.left), dfs(node.right))

        dfs(root)
        return mdia 