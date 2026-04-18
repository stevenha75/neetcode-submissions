# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # base cases
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            # The current subtree is valid if both left & right subtree are valid     
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("+inf"))
        
            
