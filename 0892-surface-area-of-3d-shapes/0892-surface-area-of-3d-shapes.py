class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        d = [(0,-1),(1,0),(0,1),(-1,0)]
        result = 0
        for y, row in enumerate(grid):
            for x, cube in enumerate(row):
                cur = grid[y][x]
                # top, bottom
                result += 2 if cur > 0 else 0
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < len(grid[0]) and 0<= ny < len(grid):
                        adj = grid[ny][nx]
                        if cur > adj:
                            result += cur - adj
                    else:
                        # outside
                        result += cur
            
        return result
                    
                    
                