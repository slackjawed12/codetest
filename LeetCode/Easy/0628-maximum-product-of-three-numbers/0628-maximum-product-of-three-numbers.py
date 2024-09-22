from typing import List
# sort - O(nlogn)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pos = self.product(nums[-3:])
        neg_two = self.product(nums[:2]+nums[-1:])
        return max(pos, neg_two)
    
    def product(self, nums: List[int]) -> int:
        result = 1
        for n in nums:
            result *= n
        
        return result

import heapq
class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        min_heap = nums[:3]
        max_heap = [-n for n in nums[:2]]
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        for n in nums[2:]:
            max_heap = self.swap_min(n, max_heap)
        for n in nums[3:]:
            min_heap = self.swap_max(n, min_heap)

        prod1 = 1
        for n in min_heap:
            prod1 *= n
        
        return max(prod1, max(min_heap) * max_heap[0] * max_heap[1])

    def swap_min(self, num:int, max_heap:List[int]) -> List[int]:
        m = heapq.heappop(max_heap)
        heapq.heappush(max_heap, m if num > -m else -num)
        return max_heap
    
    def swap_max(self, num:int, min_heap:List[int]) -> List[int]:
        m = heapq.heappop(min_heap)
        heapq.heappush(min_heap, m if num < m else num)
        return min_heap