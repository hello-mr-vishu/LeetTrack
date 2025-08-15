class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(left,right,s):
            if len(s) == 2*n:
                res.append(s)
                return
            if left<n:
                rec(left+1,right,s+'(')
            if right<left:
                rec(left,right+1,s+')')
            
        
        res = []
        rec(0,0,'')
        return res