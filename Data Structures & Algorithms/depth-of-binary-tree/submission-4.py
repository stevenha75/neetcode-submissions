# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 # tree is empty

        # put first level into q
        q = deque([root])

        level = 0

        while q:
            # retrieve cur level
            for _ in range(len(q)):
                # add children of cur lvl (construct next lvl)
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level


        