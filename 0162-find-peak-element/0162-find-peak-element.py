class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peakele = nums[0]
        peakindx = 0
        for i in range(1,len(nums)-1):
            if nums[i]>peakele and nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                peakele = nums[i]
                peakindx = i
        if nums[len(nums)-1]>peakele:
            return len(nums)-1
        return peakindx