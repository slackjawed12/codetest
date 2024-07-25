from collections import deque

class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        result = set()
        nums.sort()
        q = deque(nums)
        while q:
            mn, mx = q.popleft(), q.pop()
            result.add((mn+mx)/2)
        
        return len(result)