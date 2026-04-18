class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list -> dfs algo
        # possible base case loop -> return false
        # create a hashmap so data can be manipulated quicker and easier 
        # crs : pre
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            # base cases
            if crs in visited:
                return False # there's a loop
            elif preMap[crs] == []:
                return True # current dfs 'path' works

            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # we know current path is valid -> remove crs from visited for future paths
            visited.remove(crs)
            preMap[crs] = []

            return True

        # run dfs for each course to take care of detached graphs
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
