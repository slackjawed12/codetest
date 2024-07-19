class Solution:
    def getSmallestString(self, s: str) -> str:
        result = s
        for i in range(len(s)-1):
            c, n = s[i], s[i+1]
            if int(c) % 2 == int(n) % 2:
                swapped = s[:i]+n+c+s[i+2:]
                if int(result) > int(swapped):
                    result = swapped
                    break
            
        return result