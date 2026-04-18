class Solution:
    # sliding window approach
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tmap, smap = defaultdict(int), defaultdict(int)

        for c in t:
            tmap[c] += 1

        # build window
        l = 0
        have, need = 0, len(tmap)
        res, resLen = [0, 0], float('inf')
        for r in range(len(s)):
            # build smap
            char = s[r]
            smap[char] += 1
            if char in tmap and smap[char] == tmap[char]:
                have += 1

            while have == need:
                # save soln
                if (r - l + 1) < resLen:
                    res, resLen = [l, r], (r - l + 1)

                # move left forward 
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""