class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case (target is empty)
        if t == "": 
            return ""

        # hashmap for each string
        countT, window = {}, {}

        #init countT b/c our target doesn't move
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")

        # init window -> expand window outwards
        l = 0
        for r in range(len(s)):
            c = s[r]
            
            # update window's map
            window[c] = 1 + window.get(c, 0)

            # check if window & targ are equal (for each window expansion)
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # while window & target match (window is valid)
            while have == need:
                # update res if lower
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # shrink from left side as much as possible
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        
        l, r = res
        
        return s[l : r + 1] if resLen != float("infinity") else ""


