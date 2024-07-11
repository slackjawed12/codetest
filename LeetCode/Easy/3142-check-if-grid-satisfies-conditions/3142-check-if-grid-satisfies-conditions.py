class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = grid[i][j]
                if i < len(grid)-1:
                    below = grid[i+1][j]
                    if below != cur:
                        return False
                
                if j < len(grid[0])-1:
                    right = grid[i][j+1]
                    if right == cur:
                        return False
        
        return True