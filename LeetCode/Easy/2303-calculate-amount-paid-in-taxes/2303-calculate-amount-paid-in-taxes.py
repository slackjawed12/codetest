class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        answer = 0
        prev = 0
        for upper, percent in brackets:
            if upper <= income:
                charged = upper-prev
                answer += charged*percent/100
                prev = upper
            else:
                charged = income - prev
                answer += charged*percent/100
                break
        
        return answer