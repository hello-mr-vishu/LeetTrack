from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
      cursum = 0
      maxsum = float(-inf)
      # print(maxsum)
      for i in range(len(nums)):
        cursum += nums[i]
        maxsum = max(maxsum,cursum)
        # print(cursum)
        if cursum<0:
          cursum = 0
        # print(maxsum)
        
      return maxsum