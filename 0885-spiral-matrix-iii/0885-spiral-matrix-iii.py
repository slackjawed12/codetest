class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        class Clock:
            d = [(1,0), (0,1), (-1,0), (0,-1)]
            idx = 0
            length = 1
            prev = 0
            cur_step = 0
            def tick(self, x, y) -> List[int]:
                x = x + self.d[self.idx][0]
                y = y + self.d[self.idx][1]
                self.cur_step += 1
                if self.cur_step == self.length:
                    self.cur_step = 0
                    self.rotate()
                    if self.prev == self.length:
                        self.length += 1
                    else:
                        self.prev = self.length
                return [x,y]
            
            def rotate(self):
                self.idx = (self.idx+1)%(len(self.d))
                
        x, y = cStart, rStart
        result = [[y,x]]
        clock = Clock()
        while len(result) < rows*cols:
            x, y = clock.tick(x, y)
            if self.inRange(x, y, rows, cols):
                result.append([y,x])

        return result
    
    def inRange(self, x,y,row,col):
        return 0 <= x < col and 0 <= y < row