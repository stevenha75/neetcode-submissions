class Solution:
    # sorting? -> leads to nlogn soln
    # o(nlogn) time, o(n) space
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mheap = []

        for x, y in points:
            dist = self.dist(x, y)
            heapq.heappush(mheap, (-dist, x, y))

            # limit size of heap to k 
            if len(mheap) > k:
                heapq.heappop(mheap)

        res = []
        while mheap:
            dist, x, y = heapq.heappop(mheap)
            res.append([x, y])
        return res

    def dist(self, xi, yi):
        return (0 - xi)**2 + (0 - yi)**2