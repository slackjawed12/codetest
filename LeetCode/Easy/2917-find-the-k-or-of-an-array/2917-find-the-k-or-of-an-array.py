class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        bits = [0] * 32
        
        for num in nums:
            i = 0
            while num:
                if num & 1:
                    bits[i] += 1
                
                i += 1
                num = num // 2
        
        result = 0
        for i, bit in enumerate(bits):
            if bit >= k:
                result |= 1 << i 
        
        return result
                