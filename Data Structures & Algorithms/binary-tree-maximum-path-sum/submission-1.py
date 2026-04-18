# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # update result 
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return the path as if you're not splitting -> b/c you can only split once
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]