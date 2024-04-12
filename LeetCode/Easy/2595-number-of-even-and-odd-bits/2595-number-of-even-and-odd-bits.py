class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        temp = n
        index = 0
        answer = [0,0]
        while temp != 0:
            r = temp & 1
            if r:
                if index % 2 == 1:
                    answer[1] += 1
                else:
                    answer[0] += 1

            temp = temp >> 1
            index += 1

        return answer
