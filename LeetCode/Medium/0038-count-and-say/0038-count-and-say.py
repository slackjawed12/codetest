class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        return self.rle(self.countAndSay(n-1))
    
    def rle(self, s:str) -> str:
        result = ""
        prev, count = s[0], 1
        for i in range(1,len(s)):
            cur = s[i]
            if cur == prev:
                count += 1
            else:
                result += str(count) + str(prev)
                prev = cur
                count = 1
        
        result += str(count) + str(prev)
        return result
                
                