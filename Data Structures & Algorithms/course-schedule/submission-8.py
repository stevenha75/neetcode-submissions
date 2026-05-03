class Solution:
    # finding cycles 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        # building adjacency list (dir. graph)
        for a, b in prerequisites:
            graph[a].append(b)

        # state (unvisited 0, visiting 1, visited 2)
        state = [0] * numCourses
        
        # loop detection
        def dfs(node):
            # base cases
            if state[node] == 1:
                return True # cycle!
            if state[node] == 2:
                return False 

            # visit!
            state[node] = 1

            # visit neighbors
            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            state[node] = 2
            return False 
        
        # loop detection for each course
        for c in range(numCourses):
            if dfs(c):
                return False 
        return True 

       
