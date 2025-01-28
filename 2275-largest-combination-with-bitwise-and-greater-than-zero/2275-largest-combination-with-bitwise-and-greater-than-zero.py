class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        mask = 1
        result = 0
        while mask <= 10**8:
            temp = [num for num in candidates if num & mask]
            if len(temp) > result:
                result = len(temp)
            
            mask *= 2

        return result
            
            
