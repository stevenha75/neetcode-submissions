class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []

        for i in range(n + 1):
            temp = i
            count = 0

            while temp > 0:
                if temp & 1:
                    count += 1
                temp = temp >> 1
            
            arr.append(count)
        
        return arr