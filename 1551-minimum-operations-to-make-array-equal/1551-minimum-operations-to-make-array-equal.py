class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n//2) ** 2
        
        return (n//2) * (n//2+1)