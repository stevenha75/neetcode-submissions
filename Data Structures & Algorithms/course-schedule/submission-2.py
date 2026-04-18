class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        # fill in preMap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(crs):
            # base cases
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)

            # check each prereq
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            preMap[crs] = []
            visit.remove(crs)
            return True

        # run dfs on all courses to check for loops on all detached graphs
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        