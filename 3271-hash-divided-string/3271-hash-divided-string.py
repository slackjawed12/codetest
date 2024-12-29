class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        
        for i in range(len(s)):
            if (i+1)%k == 0:
                tmp = 0
                for j in range(i-k+1, i+1):
                    tmp += ord(s[j])-ord('a')
            
                result += chr(tmp%26+ord('a'))
                    
        return result
        