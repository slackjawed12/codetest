# slow
class neighborSum:

    def __init__(self, grid: list[list[int]]):
        self.mat = grid
        

    def adjacentSum(self, value: int) -> int:
        result = 0
        d = [(0,-1), (1,0), (0,1),(-1, 0)]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if self.mat[i][j] != value:
                    continue

                for dx, dy in d:
                    nx, ny = j+dx, i+dy
                    if 0 <= nx < len(self.mat[0]) and 0 <= ny < len(self.mat):
                        result += self.mat[ny][nx]
                
        return result
        

    def diagonalSum(self, value: int) -> int:
        result = 0
        d = [(-1,-1), (-1,+1), (+1,-1),(1,1)]
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if self.mat[i][j] != value:
                    continue
                
                for dx, dy in d:
                    nx, ny = j+dx, i+dy
                    if 0 <= nx < len(self.mat[0]) and 0 <= ny < len(self.mat):
                        result += self.mat[ny][nx]

        return result

# fast
class neighborSumV2:
    adj_d = [(0,-1), (1,0), (0,1),(-1, 0)]
    diag_d = [(-1,-1), (-1,+1), (+1,-1),(1,1)]
    def __init__(self, grid: list[list[int]]):
        self.mat = grid
        self.pos = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.pos[grid[i][j]] = (j,i)
        

    def adjacentSum(self, value: int) -> int:
        result = 0
        x, y = self.pos[value]

        for dx, dy in self.adj_d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(self.mat[0]) and 0 <= ny < len(self.mat):
                result += self.mat[ny][nx]
                
        return result
        

    def diagonalSum(self, value: int) -> int:
        result = 0
        x, y = self.pos[value]
                
        for dx, dy in self.diag_d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(self.mat[0]) and 0 <= ny < len(self.mat):
                result += self.mat[ny][nx]

        return result
        

# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)