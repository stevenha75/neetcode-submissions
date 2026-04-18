class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case: s1 can't fit inside of s2
        if len(s1) > len(s2):
            return False 

        s1Count, s2Count = [0] * 26, [0] * 26

        # init window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # init matches
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # slide the window
        l = 0
        
        # we start at s1 b/c we already init window of size s1
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # checking new character on right side of window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # remove character from left side of window (maintaining window of size s1)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1 # maintain same window size

        return matches == 26
