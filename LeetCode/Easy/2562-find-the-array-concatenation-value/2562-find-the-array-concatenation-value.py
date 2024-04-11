from collections import deque
class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        q = deque(nums)
        val = 0
        while q:
            head = q.popleft()
            tail = None
            if q:
                tail = q.pop()
            concat = str(head)+ (str(tail) if tail is not None else "")
            val += int(concat)
        
        return val
            