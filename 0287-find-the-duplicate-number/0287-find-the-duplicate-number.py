class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0, 0
        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        ptr = 0
        while True:
            slow = nums[slow]
            ptr = nums[ptr]
            if slow == ptr:
                break
        return slow