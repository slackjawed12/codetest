class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        
        cur = 0
        for i in range(len(s)):
            cur += ord(s[i])-ord('a')
            if (i+1)%k == 0:
                result += chr(cur%26+ord('a'))
                cur = 0
                    
        return result
        