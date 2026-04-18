# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # levelOrder -> think bfs
        # take a snapshot of the stack to get cur 'level'
        stack = []
        res = []

        # base case
        if not root:
            return []

        stack.append(root)
        while stack:
            level = []
            level_length = len(stack)

            for _ in range(level_length):
                node = stack.pop(0)
                level.append(node.val)
                
                # check if nodes exist before appending
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right) 
            res.append(level)

        return res        


