class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digit = 0
        temp = x
        while temp > 0:
            sum_of_digit += temp % 10
            temp //= 10
        
        return sum_of_digit if x % sum_of_digit == 0 else -1