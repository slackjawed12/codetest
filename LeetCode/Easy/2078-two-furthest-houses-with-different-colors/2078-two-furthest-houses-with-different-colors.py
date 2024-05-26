class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        answer = 0
        for i in range(0, len(colors)-1):
            for j in range(i+1, len(colors)):
                if colors[i]!=colors[j]:
                    answer= max(answer, j-i)
                
        return answer