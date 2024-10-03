class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        cur = abs(n)
        a = 1/x if n < 0 else x
        while cur > 0:
            if cur & 1:
                result *= a
            a = a*a
            cur = cur >> 1
            
        return result
        
        