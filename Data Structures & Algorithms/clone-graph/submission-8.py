"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        # mapping old : dupe
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]

            dupe = Node(node.val)
            visited[node] = dupe

            for nei in node.neighbors:
                dupe.neighbors.append(dfs(nei))
                        
            return dupe
        
        return dfs(node)
