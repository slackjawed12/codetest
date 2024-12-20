class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_mx = []
        col_mx =[]
        for row in grid:
            row_mx.append(max(row))
        for i in range(len(grid[0])):
            col = [row[i] for row in grid]
            col_mx.append(max(col))
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                result += (min(row_mx[i], col_mx[j])) - grid[i][j]

        return result