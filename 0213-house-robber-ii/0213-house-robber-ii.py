class Solution:
    def rob(self, nums: List[int]) -> int:
        def roblinear(nums):
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

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        case1 = roblinear(nums[:-1])
        case2 = roblinear(nums[1:])
        return max(case1,case2)