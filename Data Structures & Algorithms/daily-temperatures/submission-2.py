class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        
        for i in range(len(temperatures)):
            # base case, last val
            if i == len(temperatures) - 1:
                res.append(0)
                break

            temp = 0

            for j in range(i + 1, len(temperatures)):
                temp += 1

                if temperatures[i] < temperatures[j]:
                    res.append(temp)
                    break
                elif j == len(temperatures) - 1: # never found a larger value
                    res.append(0)
                    break
        
        return res



