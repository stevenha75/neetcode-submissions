class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += w
            res += "#;"

        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        return s.split("#;")[:-1]
    

# possible solns: create a string with a complex delimiter
# ...
