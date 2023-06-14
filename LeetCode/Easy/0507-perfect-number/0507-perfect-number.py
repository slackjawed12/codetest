class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        
        i = 1
        s = 0
        while i * i <= num:
            if num % i == 0:
                s += i + num//i
            i+=1
        
        return s-num == num