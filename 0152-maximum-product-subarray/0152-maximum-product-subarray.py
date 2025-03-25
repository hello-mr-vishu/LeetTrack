class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        ans = float('-inf')
        pref = 1
        suf = 1
        n = len(arr)
        for i in range(n):
            if pref == 0:
                pref = 1
            if suf == 0:
                suf = 1
            pref *= arr[i]
            suf*= arr[n-i-1]
            ans = max(ans,max(pref,suf))
        return ans