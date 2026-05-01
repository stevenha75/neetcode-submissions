class Solution:
    # soln: max heap of size k
    # why? we want to pop largest dist
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mheap = []

        for x, y in points:
            # dist from center
            dist = x**2 + y**2
            heapq.heappush(mheap, (-dist, x, y))

            if len(mheap) > k:
                heapq.heappop(mheap)
        
        res = []
        for dist, x, y in mheap:
            res.append([x, y])

        return res
