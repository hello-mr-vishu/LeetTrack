class Solution:
    def myPow(self, x: float, n: int) -> float:
        def find(x,n):
          if x==0: return 0
          if n==0: return 1
          
          res = find(x,n//2)
          res = res *res
          return x*res if n%2 else res
        res = find(x,abs(n))
        return res if n>=0 else 1/res
        