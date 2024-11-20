class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            # 해당 숫자를 포함한다.
            dfs(i + 1)
            subset.pop()
            # 해당 숫자를 포함하지 않는다.
            dfs(i + 1)

        dfs(0)
        return res
