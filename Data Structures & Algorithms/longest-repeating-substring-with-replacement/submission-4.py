class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {} # char : frequency
        res = 0

        # init sliding window on string
        L = 0
        maxf = 0
        
        # expand window as much as possible
        for R in range(len(s)):
            freq[s[R]] = 1 + freq.get(s[R], 0)
            maxf = max(maxf, freq[s[R]])

            # validate window
            while ((R - L + 1) - maxf > k):
                freq[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1) # update res if current window is the new max

        return res