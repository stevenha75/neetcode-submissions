class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vi = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in vi:
                return [vi[temp], i + 1]
            # visit
            vi[numbers[i]] = i + 1
        return []
            
