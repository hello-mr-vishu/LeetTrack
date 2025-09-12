class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case if there are no stairs or only one stair
        # if n==0 or n==1:
        #     return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        
        # Memoization
        # memo = [-1]*(n+1)
        # def ways(n,memo):
        #     if n==0 or n==1:
        #         return 1
        #     # if the result for this subproblem is 
        #     # already computed then return it
        #     if memo[n] != -1 :
        #         return memo[n]
        #     memo[n] = ways(n-1,memo)+ways(n-2,memo)
        #     return memo[n]
        # return ways(n,memo)

        # one , two = 1,1
        # for i in range(n-1):
        #     temp = one
        #     one = one+two
        #     two = temp
        # return one

        def rec(n):
            if n == 1 or n == 0:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = rec(n-1) + rec(n-2)
            return dp[n]
        dp = [-1]*(n+1)
        # for i in range(n):
            # dp[i] == -1
        return rec(n)