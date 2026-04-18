# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # returns(balanced?: Bool, height: int)
        def dfs(node):
            if not node:
                return (True, 0)

            # balanced conditions:
            # left + right balanced + height diff <=1 
            left = dfs(node.left)
            right = dfs(node.right)

            # base case: if anything is unbalanced -> whole true is unbalanced
            if not left[0] or not right[0]:
                return (False, 0)

            balanced = ((left[0] and right[0]) and 
                        (abs(left[1] - right[1]) <= 1))

            return (balanced, 1 + max(left[1], right[1])) 
        
        return dfs(root)[0] 