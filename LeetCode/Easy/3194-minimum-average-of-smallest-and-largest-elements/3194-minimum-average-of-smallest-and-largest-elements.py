from collections import deque

class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        q = deque(sorted(nums))
        avgs = []
        while q:
            mn, mx = q.popleft(), q.pop()
            avgs.append((mn+mx)/2)
        
        return min(avgs)
            