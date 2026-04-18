class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # is dictionary equality the efficient method? 
        s_dict = {}
        t_dict = {}

        for c in s:
            if c not in s_dict:
                s_dict[c] = 0
            else:
                s_dict[c] += 1

        for c in t:
            if c not in t_dict:
                t_dict[c] = 0
            else:
                t_dict[c] += 1

        return s_dict == t_dict
