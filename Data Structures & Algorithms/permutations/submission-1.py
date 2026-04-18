class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path, visited):
            if len(path) == len(nums):
                # path completed
                res.append(path[:])
                return

            for i in range(0, len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    dfs(path, visited)
                    path.pop()
                    visited.remove((nums[i]))

        dfs([], set())
        return res

        