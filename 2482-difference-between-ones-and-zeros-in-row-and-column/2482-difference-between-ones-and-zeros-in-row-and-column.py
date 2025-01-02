class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n =len(grid), len(grid[0])
        one_row, one_col = self.ones(grid)
        diff= [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = 2*one_row[i] + 2*one_col[j] - m - n
        
        return diff
    
    def ones(self, grid: List[List[int]]) -> (List[int], List[int]):
        one_row = []
        for i in range(len(grid)):
            one_row.append(sum(grid[i]))
        
        one_col = []
        for i in range(len(grid[0])):
            acc = 0
            for j in range(len(grid)):
                acc += grid[j][i]
            
            one_col.append(acc)
        
        return one_row, one_col