class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        first = True
        for c in s:
            if first:
                if c == '1':
                    continue
                else:
                    first = False
            else:
                if c == '1':
                    return False
                
        return True