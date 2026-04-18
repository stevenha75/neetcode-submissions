# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # case 1: we split here -> we are @ LCA
        # case 2: from here -> we only found p or q -> it must be in this subtree
            
        def dfs(node):
            if not node:
                return None 
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right
            
        return dfs(root)

