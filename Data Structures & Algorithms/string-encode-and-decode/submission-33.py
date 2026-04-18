class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for w in strs:
            res += (str(len(w)) + '#' + w) 

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            print(s[i:j])
            length = int(s[i:j])
            
            # getting word
            i = j + 1 
            j = i + length
            word = s[i:j]

            res.append(word)

            i = j # set to start of next num
        
        return res
