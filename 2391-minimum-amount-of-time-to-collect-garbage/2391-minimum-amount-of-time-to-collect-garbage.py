class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        paper =  self.getTime(garbage, travel, "P") 
        glass = self.getTime(garbage, travel, "G")
        metal =  self.getTime(garbage, travel, "M")
        return paper + glass + metal
        
    def getTime(self, garbage: List[str], travel: List[int], gtype:str):
        last = -1
        for i in range(len(garbage)-1, -1, -1):
            if gtype in set(garbage[i]):
                last = i
                break
        
        if last == -1:
            return 0
        
        result = 0
        for i in range(last+1):
            result += self.count(garbage[i], gtype)
            if i != last:
               result += travel[i]
            
        return result
    
    def count(self, st:str, target:str):
        cnt = 0
        for c in st:
            if c == target:
                cnt += 1
        return cnt