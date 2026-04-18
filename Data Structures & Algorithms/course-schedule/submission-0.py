class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        # fill in map 
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visit set to detect loop in curr path
        visit = set()

        def dfs(crs):
            # base cases
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            # we know the current crs in unvisited
            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
        
            visit.remove(crs)
            preMap[crs] = []
            return True

        # run for every course to find loops in detached graphs
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True



        