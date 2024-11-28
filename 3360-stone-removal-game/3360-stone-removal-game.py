class Solution:
    def canAliceWin(self, n: int) -> bool:
        cur =10
        a = False
        while n - cur >= 0:
            a = not a
            n -= cur
            cur -= 1
        
        return a