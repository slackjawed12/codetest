class Solution:
    def checkString(self, s: str) -> bool:
        a = -1
        b = len(s)
        for i, c in enumerate(s):
            if c == 'a':
                a = i
            else:
                if b == len(s):
                    b = i

        return a < b
        
                