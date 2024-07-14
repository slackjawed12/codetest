from collections import defaultdict
class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        result = 0
        for k, v in counter.items():
            if v == 2:
                result ^= k
        
        return result