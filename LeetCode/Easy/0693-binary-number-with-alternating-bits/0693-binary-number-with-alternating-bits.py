class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        one = n & 1
        while n > 0:
            n = n >> 1
            cur = n & 1
            if one:
                if cur:
                    return False
            else:
                if not cur:
                    return False

            one = cur
            
        return True
