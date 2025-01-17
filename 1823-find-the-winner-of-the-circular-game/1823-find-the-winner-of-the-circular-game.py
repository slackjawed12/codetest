class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1,n+1))

        last = 0
        while q:
            for i in range(k-1):
                q.append(q.popleft())

            last = q.popleft()
        
        return last
