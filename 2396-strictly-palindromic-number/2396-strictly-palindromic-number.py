class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        s = str(bin(n))[2:]
        for b in range(2, n-1):
            s = self.base(n, b) 
            if not self.palindrome(s):
                return False
        
        return True
    
    def base(self, n: int, b:int) -> str:
        t = n
        r = ""
        while t:
            r += str(t%b)
            t //= b
        
        return r
            
    
    def palindrome(self, s:str) -> bool:
        # 6 - 0, 1, 2
        # 5 - 0, 1, 2
        # 4 - 0, 1
        # 3 - 0, 1
        l = len(s)
        e = l // 2 if l % 2 else l//2-1
        for i in range(len(s)//2):
            if s[i] != s[l-i-1]:
                return False

        return True
        
        