class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # o(n) space + timew
        if len(s) != len(t):
            return False

        sdict, tdict = defaultdict(int), defaultdict(int)
        
        # build a dict for both
        for i in range(len(s)):
            sdict[s[i]] += 1
            tdict[t[i]] += 1

        # dict comparison
        return sdict == tdict 
