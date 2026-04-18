class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force soln
        cache = defaultdict(list)

        for s in strs:
            # sorting word
            key = ''.join(sorted(s))
            cache[key].append(s)
        
        return list(cache.values())

        