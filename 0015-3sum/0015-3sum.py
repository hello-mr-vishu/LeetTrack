class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = set()
        nums.sort()

        # print(nums)
        for i in range(len(nums)-2):
            s= 0
            leftptr = i+1
            rightptr = len(nums)-1
            while leftptr<rightptr:
                s = nums[i]+nums[leftptr]+nums[rightptr]
                if s == 0:
                    lst.add((nums[i],nums[leftptr],nums[rightptr]))
                    leftptr+=1
                    rightptr-=1
                elif s<0:
                    leftptr+=1
                else:
                    rightptr-=1
        return [list(triplet) for triplet in lst]