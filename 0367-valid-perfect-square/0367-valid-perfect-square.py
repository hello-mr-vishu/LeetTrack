class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd = 1
        s =1
        while s<= num:
            if s == num:
                return True
            odd+=2
            s += odd
        return False