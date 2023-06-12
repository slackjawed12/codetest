class Solution:
    def convertToBase7(self, num: int) -> str:
        answer = []
        is_negative = False
        if num < 0:
            is_negative = True
            num = abs(num)
        elif num == 0:
            return '0'

        while num != 0:
            q, r = divmod(num, 7)
            answer.append(str(r))
            num = q
            
        if is_negative:
            answer.append('-')
            
        return ''.join(reversed(answer))