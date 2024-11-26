class Solution:
    def binaryGap(self, n: int) -> int:
        b = str(bin(n))[2:]
        l=-1
        result = 0
        for r in range(len(b)):
            ch = b[r]
            if ch == '1':
                if l != -1:
                    result = max(result, r-l)
                l = r
                    
        return result