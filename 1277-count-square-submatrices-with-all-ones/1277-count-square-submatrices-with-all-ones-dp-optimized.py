class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [matrix[0][:]]+[[0]*len(matrix[0]) for _ in matrix[1:]]
        for r in range(len(matrix)):
            dp[r][0] = matrix[r][0]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        result = 0
        for row in dp:
            for num in row:
                result += num
        
        return result