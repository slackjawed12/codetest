class Solution:
    def alternateDigitSum(self, n: int) -> int:
        power = 1
        temp = n
        while temp:
            power *= 10
            temp //= 10
        
        temp = n
        power //= 10
        answer = 0
        flag = 1
        while power:
            q = flag * (temp // power)
            answer += q
            temp = temp % power
            power //= 10
            flag *= -1

        return answer