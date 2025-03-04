class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ht = {}
        for i in range(len(nums)):
          if nums[i] not in ht:
            ht[nums[i]]=1
          else:
            return nums[i]
        return -1      