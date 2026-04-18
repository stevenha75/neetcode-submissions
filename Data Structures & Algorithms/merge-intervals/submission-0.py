class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
    
        # either merge w/ last or add
        for start, end in intervals[1:]:
            last_end = output[-1]
            
            # overlap case
            if last_end[1] >= start:
                output[-1][1] = max(end, last_end[1])
            else:
                output.append([start, end])

        return output