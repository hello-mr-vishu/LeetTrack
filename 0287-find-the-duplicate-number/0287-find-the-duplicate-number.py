class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ptr1 , ptr2 = 0,0
        while True:
            ptr1 = nums[ptr1]
            ptr2 = nums[nums[ptr2]]
            if ptr1 == ptr2:
                break
        ptr1 = 0
        while True:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
            if ptr1==ptr2:
                break
        return ptr1