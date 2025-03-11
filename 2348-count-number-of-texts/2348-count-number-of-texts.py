class Solution:
    def countTexts(self, x: str) -> int:
        l=len(x)
        @lru_cache(None)
        def f(i):
            if i==l:return 1
            ans=0
            for j in range(i,i+(4 if x[i] in '97' else 3)):
                    if j<l and x[j]==x[i]:
                        ans+=f(j+1)
                    else:
                        break
            return ans%(10**9+7)
        return f(0)