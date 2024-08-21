class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        result = 1000000
        for n in nums:
            dist = abs(n)
            if dist < abs(result):
                result = n
            elif dist == abs(result):
                result = max(n, result)
        
        return result
            
        