class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)

        def fun(idx):
            if idx == 0:
                return nums[0]
            if idx < 0:
                return 0
            if dp[idx]!= -1:
                return dp[idx]
            pick = nums[idx]+ fun(idx-2)
            notpick= 0 + fun(idx-1)
            dp[idx] = max(pick,notpick)
            return dp[idx]
        return fun(len(nums)-1)