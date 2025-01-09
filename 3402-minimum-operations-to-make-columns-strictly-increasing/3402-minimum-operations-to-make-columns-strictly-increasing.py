class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid[0])):
            cur = grid[0][i]
            for j in range(1, len(grid)):
                if grid[j][i] <= cur:
                    result += cur - grid[j][i] + 1
                    grid[j][i] = cur+1
                
                cur = grid[j][i]
            
        return result