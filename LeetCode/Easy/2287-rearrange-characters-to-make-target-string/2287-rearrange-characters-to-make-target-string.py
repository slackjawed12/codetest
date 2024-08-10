class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d={}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1


        result = 0
        while self.isIncluded(d, target):
            result += 1
        
        return result
    
    def isIncluded(self, d: dict, target: str) -> bool:
        for c in target:
            if c not in d or d[c] < 1:
                return False

            d[c] -= 1
        
        return True
        