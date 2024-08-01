import heapq
from math import floor, sqrt

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        rev = [-v for v in gifts]
        heapq.heapify(rev)
        for i in range(k):
            mx = -heapq.heappop(rev)
            sub = floor(sqrt(mx))
            mx = sub
            heapq.heappush(rev, -mx)
        
        return sum([-v for v in rev])
