# 극장 좌석
import sys


class Solution:
    def __init__(self):
        self.seats = int(sys.stdin.readline().strip())
        m = int(sys.stdin.readline().strip())
        self.fixed = [int(sys.stdin.readline().strip()) for _ in range(m)]

    def get_combination(self):
        pibo = [0] * 41
        pibo[0], pibo[1] = 1, 1
        for i in range(2, len(pibo)):
            pibo[i] = pibo[i - 1] + pibo[i - 2]

        partitions = []
        start = 1
        for f in self.fixed:
            partitions.append(f - start)
            start = f + 1

        partitions.append(self.seats - start + 1)
        
        answer = 1
        for p in partitions:
            answer *= pibo[p]

        return answer

    
sol = Solution()
print(sol.get_combination())
