class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # ------Binary Search-------
        nums.sort()
        left = 0
        right = len(nums)
        while left<right:
            mid = (left+right)//2
            if nums[mid]==target:
                return True
            elif target>nums[mid]:
                left = mid+1
            else:
                right = mid
        return False






        # --------Brute Force------------
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return True
        # return False