class Solution:
    def countBits(self, n: int) -> List[int]:
        # personal bruteforce soln
        # looping 0 -> n 
        soln = []

        for i in range(n + 1):
            cur = i
            one_count = 0
            while cur > 0:
                if cur % 2 == 1: # remainder
                    one_count += 1
                cur = cur // 2 # qoutient
            soln.append(one_count)
        
        return soln

