class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        result = derived[0]
        for i in range(1,len(derived)):
            result = result ^ derived[i]
        
        return not result