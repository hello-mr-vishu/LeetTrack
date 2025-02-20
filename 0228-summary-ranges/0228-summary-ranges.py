from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        lst = []
        i = 0 
        
        while i < len(nums):
            start = nums[i] 
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:  
                i += 1  
            
            if start == nums[i]:  
                lst.append(str(start))  
            else:
                lst.append(f"{start}->{nums[i]}")  
            
            i += 1  

        return lst
