class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # bruteforce soln?
        # some type of bucket?
        buckets = defaultdict(list)
        # sorted_word : [orig, ]

        # build buckets
        for w in strs:
            sorted_w = ''.join(sorted(w))
            buckets[sorted_w].append(w)

        return buckets.values()

        



        