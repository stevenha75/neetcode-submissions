class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for s in strs:
            sentence = sentence + s + ";]"
        return sentence

    def decode(self, s: str) -> List[str]:
        # edge case -> empty string
        if s == ";]":
            return [""]
        elif not s:
            return []

        soln = s.split(";]")
        soln.pop()
        
        return soln
        
