class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case if there are no stairs or only one stair
        # if n==0 or n==1:
        #     return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        memo = [-1]*(n+1)
        def ways(n,memo):
            if n==0 or n==1:
                return 1
            # if the result for this subproblem is 
            # already computed then return it
            if memo[n] != -1 :
                return memo[n]
            memo[n] = ways(n-1,memo)+ways(n-2,memo)
            return memo[n]
        return ways(n,memo)