class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # case: new fits before cur
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # case: new comes after cur 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # case: merge necessary
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                               max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res