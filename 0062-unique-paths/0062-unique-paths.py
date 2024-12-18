class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(n):
            if n ==1 or n == 0:
                return 1
            return f(n-1) * n
            
        return f(m+n-2) // f(m-1) // f(n-1)