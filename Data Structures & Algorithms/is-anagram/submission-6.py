class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = defaultdict(int)
        tdict = defaultdict(int)
        
        # build a dict for both
        for c in s:
            sdict[c] +=1
        for c in t:
            tdict[c] += 1 

        # dict comparison
        return sdict == tdict 