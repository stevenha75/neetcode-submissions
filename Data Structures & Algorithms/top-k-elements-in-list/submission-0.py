class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # efficient soln (bucket sort)
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        # setup buckets
        for n, c in count.items():
            freq[c].append(n)
        
        res = []

        # loop through freq backwards (largest freq first)
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




