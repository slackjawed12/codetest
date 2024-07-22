class Solution:
    def minChanges(self, n: int, k: int) -> int:
        result = 0
        while n or k:
            nb = n & 1
            kb = k & 1
            if nb == 1 and kb == 0:
                result += 1
            elif nb == 0 and kb ==1:
                result = -1
                break

            n = n >> 1
            k = k >> 1
        
        return result
                