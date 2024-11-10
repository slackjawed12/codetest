class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        cur = n
        while self.productDigit(cur) % t != 0:
            cur += 1
        
        return cur
    
    def productDigit(self, num:int) -> int:
        result = 1
        while num:
            result *= num % 10
            num //= 10
        
        return result
        