class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def odd(s:str)->bool:
            return int(s) % 2 == 1
        
        def odd_a(s:str)->bool:
            return int(ord(s)-ord('a')) % 2 == 1
        
        def white(c:str)->bool:
            if odd(c[1]):
                return not odd_a(c[0])
            
            return odd_a(c[0])
        
        if white(coordinate1):
            return white(coordinate2)
        
        return not white(coordinate2)