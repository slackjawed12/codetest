class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        m = 0
        tmp = n
        while tmp:
            tmp = tmp >> 1
            m += 1
        
        mask = ~0 << m
        return ~n ^ mask
        