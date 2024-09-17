class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y,m,d = date.split("-")
        return self.binary(y) + "-" + self.binary(m) + "-" + self.binary(d)
    
    def binary(self, num:str)->str:
        i = int(num)
        result = ""
        while i:
            result = str(i % 2) + result
            i //= 2
        
        return result
            
        
        