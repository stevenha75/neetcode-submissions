class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # back tracking soln
        res = []
        nums.sort()

        def dfs(i, path, total):
            # base case
            if total == target:
                res.append(path[:])
                return 
            elif total > target:
                return

            # explore diff paths
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, path, total + nums[j])
                path.pop()

        dfs(0, [], 0)
        return res 