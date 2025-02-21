class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort()
        # print(intervals)
        newinterval = []
        res = []
        newinterval = intervals[0]
        # print(newinterval)
        for i in intervals[1:]:
            if i[0] <= newinterval[1]:
                newinterval[1] = max(newinterval[1],i[1])
            else:
                res.append(newinterval)
                newinterval = i
        res.append(newinterval)
        return res