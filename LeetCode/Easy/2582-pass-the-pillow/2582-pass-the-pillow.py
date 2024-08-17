# linear
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        reverse = False
        for t in range(time):
            if cur == n:
                reverse = True
            
            if cur == 1:
                reverse = False
            
            cur += 1 if not reverse else -1

        return cur
                
            
# math
class Solution2:
    def passThePillow(self, n: int, time: int) -> int:
        t = time % (2*n -2)
        return t+1 if t <= n-1 else abs(-t + 2*n-1)