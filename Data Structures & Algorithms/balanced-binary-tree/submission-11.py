# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs where we calc height?
        # a helper would be nice? 
        def dfs(node):
            if not node:
                # (height, balanced)
                return (0, True)
            
            # we need L + R height to determine balance
            # can't think of a clean way to handle both ops?
            left = dfs(node.left)
            right = dfs(node.right)
            balance = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            return (1 + max(left[0], right[0]), balance)

        return dfs(root)[1]