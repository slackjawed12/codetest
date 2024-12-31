class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)
        result = 0
        while q:
            q.popleft()
            q.pop()
            result += q.pop()
        
        return result
