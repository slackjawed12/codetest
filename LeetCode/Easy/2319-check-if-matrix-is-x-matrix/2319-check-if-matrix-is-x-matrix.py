class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if j == i or j == n-i-1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False

        return True
            