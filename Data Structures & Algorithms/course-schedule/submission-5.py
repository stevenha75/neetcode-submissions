class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Ex2: -> shows we are looking for loops
        # -> easiest way to do this is w/ graphs
        # -> Treat pr[i] = adjacency list
        # -> lets convert this to a dict for faster look up 

        dict = {}

        for course, prereq in prerequisites:
            if course not in dict:
                dict[course] = []
            dict[course].append(prereq)

        visited = set()
        def dfs(course):
            # base cases
            if course in visited:
                return False # there's a loop in this case
            if course not in dict:
                return True # -> can take this course

            # visit
            visited.add(course)

            # loop through each prereq of course
            for prereq in dict[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course) # so future paths can visit course
            dict[course] = [] # saves duplicate work

            return True

        # Make sure you can take each course
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


