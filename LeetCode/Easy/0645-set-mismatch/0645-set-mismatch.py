from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        for n in range(1, len(nums)+1):
            xor ^= n
        rightmost = xor & ~(xor-1)
        setbit = 0
        not_setbit = 0
        for n in nums:
            if n & rightmost:
                setbit ^= n
            else:
                not_setbit ^= n
        
        for n in range(1, len(nums)+1):
            if n & rightmost:
                setbit ^= n
            else:
                not_setbit ^= n

        return [setbit, not_setbit] if setbit in nums else [not_setbit, setbit]