class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [0] + [0] * len(nums)
        dp1[1] = nums[0]  # 첫 번째 집 텀

        dp2 = [0] + [0] * len(nums)
        dp2[1] = 0  # 첫 번째 집 안 텀

        for n in range(2, len(dp1)):
            dp1[n] = max(dp1[n - 2] + nums[n - 1], dp1[n - 1])
            dp2[n] = max(dp2[n - 2] + nums[n - 1], dp2[n - 1])

        return max(dp1[-2], dp2[-1])
