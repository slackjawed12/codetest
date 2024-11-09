import heapq
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        store = []
        heapq.heapify(store)
        for n in nums:
            if len(store) <= 1:
                heapq.heappush(store, -n)
                continue
            
            first, second = [-heapq.heappop(store) for i in range(2)]
            if first >= n and second >= n:
                return False
            
            heapq.heappush(store, -first)
            heapq.heappush(store, -second)
            heapq.heappush(store, -n)

        return True
        
        