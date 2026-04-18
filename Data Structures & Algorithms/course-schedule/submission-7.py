class Solution:
    # finding cycles 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        # 1) adjacency list to graph
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        # visited state (if we revisit node -> cycle)
        state = [0] * numCourses
        # 0 -> unvisited
        # 1 -> visiting (current call)
        # 2 -> visited

        # dfs -> look for cycles
        def dfs(node):
            # base cases
            if state[node] == 1:
                return True # cycle 
            elif state[node] == 2:
                return False
            
            # visit cur + recurse
            state[node] = 1
            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            state[node] = 2
            return False

        # account for islands
        for i in range(numCourses):
            if dfs(i): # cycle case
                return False # can't finish courses

        return True 