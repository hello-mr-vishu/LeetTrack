from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        lst = []
        start = nums[0]  

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    lst.append(str(start))
                else:
                    lst.append(f"{start}->{nums[i-1]}")
                start = nums[i]  
        if start == nums[-1]:
            lst.append(str(start))
        else:
            lst.append(f"{start}->{nums[-1]}")

        return lst
