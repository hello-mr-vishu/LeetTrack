class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 0:
            return 0
        if n==1:
            return nums[0]
        last = max(nums[0],nums[1])
        secondlast = nums[0]
        for i in range(2,n):
            pick = nums[i]+secondlast
            notpick = last
            curr = max(pick,notpick)
            secondlast = last
            last = curr
        return last
        
        # dp = [0]*(n+1)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])
        # # res = 0
        # for i in range(2,n):
        #     pick = nums[i] + dp[i-2]   # (rob current + skip previous)
        #     notpick = 0 + dp[i-1]
        #     dp[i] = max(pick,notpick)
        # return dp[n-1]

        # n = len(nums)
        # dp = [-1]*(n)

        # def fun(idx):
        #     if idx == 0:
        #         return nums[0]
        #     if idx < 0:
        #         return 0
        #     if dp[idx]!= -1:
        #         return dp[idx]
        #     pick = nums[idx]+ fun(idx-2)
        #     notpick= 0 + fun(idx-1)
        #     dp[idx] = max(pick,notpick)
        #     print(dp)
        #     return dp[idx]

        # return fun(len(nums)-1)
