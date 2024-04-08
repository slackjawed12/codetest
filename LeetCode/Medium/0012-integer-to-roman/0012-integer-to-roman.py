class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        temp = num
        q, r = divmod(temp, 1000)
        if q != 0:
            answer += "M"*q
            temp = r

        q, r = divmod(temp, 100)
        if q != 0:
            if q < 4:
                answer += "C"*q
            elif q == 4:
                answer += "CD"
            elif q == 9:
                answer += "CM"
            else:
                answer += ("D" + "C"*(q-5))
            temp = r

        q, r = divmod(temp, 10)
        if q != 0:
            if q < 4:
                answer += "X"*q
            elif q == 4:
                answer += "XL"
            elif q == 9:
                answer += "XC"
            else:
                answer += ("L" + "X"*(q-5))
            temp = r
        
        r = temp % 10
        if r != 0:
            if r < 4:
                answer += "I"*r
            elif r == 4:
                answer += "IV"
            elif r == 9:
                answer += "IX"
            else:
                answer += ("V" + "I"*(r-5))

        return answer