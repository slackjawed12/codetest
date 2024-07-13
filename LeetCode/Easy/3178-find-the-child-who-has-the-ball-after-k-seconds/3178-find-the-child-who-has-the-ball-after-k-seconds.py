class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cur = 0
        time = 0
        reverse = False
        while time != k:
            if reverse:
                cur -= 1
                if cur == 0:
                    reverse = False
            else:
                cur += 1
                if cur == n-1:
                    reverse = True
            
            time += 1
        
        return cur

# using periodic feature solution
# every 2*(n-1) seconds, the ball will return to the first child
# so we can use k % (2*(n-1)) to get the final position of the ball
class Solution2:
    def numberOfChild(self, n: int, k: int) -> int:
        nk = k % (2 * (n - 1))
        return nk if nk < n else 2 * n - 2 - nk
