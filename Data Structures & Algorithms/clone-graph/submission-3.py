"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # pair old:new

        def dfs(node):
            # base cases
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            
            # update visited list
            oldToNew[node] = copy

            # append the neighbors to this copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        
        return dfs(node) if node else None


        