class Solution:
    def countBits(self, n: int) -> List[int]:
        # personal bruteforce soln
        # looping 0 -> n 
        soln = []

        for i in range(n + 1):
            bin_num = bin(i) # binary num
            count = bin_num.count('1')
            soln.append(count)
        
        return soln

