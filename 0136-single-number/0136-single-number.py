class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ht = {}
        for i in range(len(nums)):
          if nums[i] not in ht:
            ht[nums[i]] = 1
          else:
            ht[nums[i]]+=1
        for j in ht:
          if ht[j] == 1:
            return j
        return None