class Solution:
    # sorting? -> leads to logn soln
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dlist = []
        
        for p in points:
            xi, yi = p
            pdist = self.dist(xi, yi)
            dlist.append((p, pdist))

        dlist.sort(key=lambda e: e[1])

        for i in range(k):
            res.append(dlist[i][0])
        
        return res

    def dist(self, xi, yi):
        return math.sqrt((0 - xi)**2 + (0 - yi)**2)