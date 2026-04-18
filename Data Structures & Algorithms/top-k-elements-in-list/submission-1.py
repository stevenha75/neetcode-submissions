class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        # now to sort dict by values (num[1] is the freq)
        sorted_dict = dict(sorted(freq.items(), key=lambda num : num[1], reverse=True))

        return list(sorted_dict.keys())[:k]




