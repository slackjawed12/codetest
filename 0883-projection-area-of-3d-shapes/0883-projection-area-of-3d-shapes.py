class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        for row in grid:
            result += len([c for c in row if c != 0])
            result += max(row)
        
        for i in range(len(grid[0])):
            col = [grid[j][i] for j in range(len(grid))]
            result += max(col)
        
        return result
           