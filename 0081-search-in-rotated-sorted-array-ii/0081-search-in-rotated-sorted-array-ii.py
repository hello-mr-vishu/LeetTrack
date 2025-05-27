class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]== target:
                return True
            if nums[left]==nums[mid]==nums[right]:
                left = left+1
                right = right-1
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return False

        
        
        
        
        
        
        
        
        
        
        
        # ------Binary Search-------
        # nums.sort()
        # left = 0
        # right = len(nums)
        # while left<right:
        #     mid = (left+right)//2
        #     if nums[mid]==target:
        #         return True
        #     elif target>nums[mid]:
        #         left = mid+1
        #     else:
        #         right = mid
        # return False






        # --------Brute Force------------
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return True
        # return False