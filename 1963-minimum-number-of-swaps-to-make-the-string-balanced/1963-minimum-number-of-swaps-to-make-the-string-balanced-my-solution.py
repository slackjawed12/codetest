class Solution:
    def minSwaps(self, s: str) -> int:
        o, c = 0, 0
        result = 0
        for i, ch in enumerate(s):
            if ch == '[':
                o += 1
            elif ch == ']':
                c += 1
            
            if c > o:
                result += 1
                o += 1
                c -= 1
    
        return result