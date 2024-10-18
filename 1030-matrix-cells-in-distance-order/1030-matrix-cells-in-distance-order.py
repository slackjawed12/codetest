class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        mat = []
        for i in range(rows):
            for j in range(cols):
                mat.append([i,j])
        
        mat.sort(key=lambda x:abs(x[0]-rCenter)+abs(x[1]-cCenter))
        return mat
        
        