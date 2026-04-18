from collections import defaultdict 

class TimeMap:

    def __init__(self):
        # key: sorted [(val, timestamp)]
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))        

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key] #[(val, timestamp)]

        # bin search for most recent timestamp
        L, R = 0, len(values) - 1
        res = ""

        while L <= R:
            M = (L + R) // 2
            prev = values[M]

            if values[M][1] == timestamp:
                return values[M][0]

            # move pointers
            if values[M][1] < timestamp:
                res = values[M][0] # save last valid ans.
                L = M + 1 
            elif values[M][1] > timestamp:
                R = M - 1 
        
        return res
        
