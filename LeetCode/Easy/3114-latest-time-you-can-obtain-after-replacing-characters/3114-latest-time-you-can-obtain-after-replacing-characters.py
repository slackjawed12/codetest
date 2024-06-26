class Solution:
    def findLatestTime(self, s: str) -> str:
        result = ""
        for i, c in enumerate(s):
            if c == '?':
                if i == 0:
                    if s[1] == '1' or s[1] == '0' or s[1] == '?':
                        result += '1'
                    else:
                        result += '0'
                elif i == 1:
                    if s[0] == '0':
                        result += '9'
                    else:
                        result += '1'
                elif i == 3:
                    result += '5'
                elif i == 4:
                    result += '9'
            else:
                result += c
        
        return result