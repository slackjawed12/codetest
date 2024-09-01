from heapq import heapify, heappop, heappush

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        pair = [(n,i) for i, n in enumerate(nums)]
        
        heapify(pair)
        for i in range(k):
            x = heappop(pair)
            heappush(pair, (x[0]*multiplier, x[1]))
        
        result = sorted([(v,i) for v, i in pair], key=lambda x:x[1])
        return [v for v, i in result]