from typing import List

class Solution:
    def recurPermute(self, nums: List[int], freq: List[int], ds: List[int], ans: List[List[int]]):
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return
        for i in range(len(nums)):
            if not freq[i]:
                ds.append(nums[i])
                freq[i] = 1
                self.recurPermute(nums, freq, ds, ans)
                freq[i] = 0
                ds.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        freq = [0] * len(nums)
        self.recurPermute(nums, freq, ds, ans)
        return ans
