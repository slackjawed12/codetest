from collections import defaultdict

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        
        result = 0
        n = len(nums)//2
        for k, v in store.items():
            if v == n:
                result = k
                break
        
        return result