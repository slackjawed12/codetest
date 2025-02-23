class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                result = max(result, self.hourglass(grid, i, j))
        
        return result
                
                
    def hourglass(self, mat: List[List[int]], row: int, col: int) -> int:
        result = 0
        for i in range(3):
            for j in range(3):
                result += mat[row+i][col+j]
        
        result -= mat[row+1][col] + mat[row+1][col+2]
        return result
                
                
        