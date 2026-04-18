class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["neet", "code"]
        # "4#neet4#code"
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        soln = []

        i = 0
        # need to find the # -> (the word comes afterwards)
        while i < len(s): # make sure you don't go out of bounds
            # i will start at the number 
            j = i 
            # j will look for the # 
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            soln.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        
        return soln
