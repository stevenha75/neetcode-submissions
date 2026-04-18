class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # decision tree
        # i -> current pos in nums
        # cur -> cur path
        def dfs(i, cur, total):
            # base cases
            if total == target:
                # we need copy b/c we are using the same reference 
                # throughout loops
                res.append(cur.copy())
                return
            if total > target or i >= len(nums):
                return

            # go down each path
            # include i 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # skip i
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res 

            