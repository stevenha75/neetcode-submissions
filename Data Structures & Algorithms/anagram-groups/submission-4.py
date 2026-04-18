class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            # how can we store the count of each letter?
            count = [0] * 26
            for c in w:
                # ord('a') - ord('a') = 0 
                count[ord(c) - ord('a')] += 1
            # now we have the count of each letter
            res[tuple(count)].append(w)

        return res.values()



        