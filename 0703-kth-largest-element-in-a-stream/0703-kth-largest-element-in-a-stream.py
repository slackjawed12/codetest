import heapq
class KthLargest:
    k: int
    heap: List[int]
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = sorted(nums) if len(nums) <= k else sorted(nums)[-k:]
        heapq.heapify(self.stream)
        print(self.stream)
        

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        else:
            if self.stream[0] > val:
                return self.stream[0]
            else:
                heapq.heappop(self.stream)
                heapq.heappush(self.stream, val)

        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)