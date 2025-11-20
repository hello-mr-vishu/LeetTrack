class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = float('-inf')
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
                cnt += 1
            elif candidate == num:
                cnt += 1
            else:
                cnt -= 1
        return candidate