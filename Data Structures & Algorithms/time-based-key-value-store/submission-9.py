class TimeMap:

    def __init__(self):
        self.dict = {} # key : [ list of [ val, timestamp ] ]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # default soln
        res = ""
        values = self.dict.get(key, [])
        
        # binary search
        l, r = 0, len(values) - 1 
        while l <= r:
            m = (l + r) // 2

            # valid res case
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                # not valid -> we want to look in left side
                r = m - 1
        
        return res



        
