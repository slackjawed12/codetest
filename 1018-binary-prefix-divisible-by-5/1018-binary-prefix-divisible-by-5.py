class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        cur = 0
        for i in nums:
            cur = (cur << 1) + i
            result.append(cur % 5 == 0)
        
        return result
            
            
            
            