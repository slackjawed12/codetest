class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        answer = []
        for i, row in enumerate(mat):
            s = sum(row)
            if len(answer) == 0:
                answer = [0,s]
            elif answer[1] < s:
                answer = [i, s]
        
        return answer