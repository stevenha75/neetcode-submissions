# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # cases for balance
    # 1) left balanced
    # 2) right balanced
    # 3) diff <= 1 
    # time o(n), space o(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # (height: int, is_balanced: bool)
        def dfs(node):
            if not node:
                return (0, True)
            
            left, right = dfs(node.left), dfs(node.right)
            lefth, righth = left[0], right[0]
            newh = 1 + max(lefth, righth)

            if left[1] and right[1] and abs(lefth - righth) <= 1:
                return (newh, True) 
            else:
                return (newh, False)

        return dfs(root)[1]
