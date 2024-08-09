class Solution:
    def countEven(self, num: int) -> int:
        result = 0
        
        for i in range(1, num+1):
            digit_sum, temp = 0, i
            while temp:
                digit_sum += temp % 10
                temp //= 10
            
            if digit_sum % 2 == 0:
                result += 1

        return result