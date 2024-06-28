from collections import defaultdict
class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                subgrid = []
                for y in range(2):
                    for x in range(2):
                        subgrid.append(grid[i+y][j+x])
                
                counter = defaultdict(int)
                for c in subgrid:
                    counter[c] += 1
                
                if counter['W'] >= 3 or counter['B'] >= 3:
                    return True
            
        return False