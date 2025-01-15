class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # row
        result = [[0]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            diag = []
            x, y = 0, i
            while 0 <= x < len(mat[0]) and 0 <= y < len(mat):
                diag.append(mat[y][x])
                x += 1
                y += 1
            
            diag.sort()
            x, y = 0, i
            while 0 <= x < len(mat[0]) and 0 <= y < len(mat):
                result[y][x] = diag[x]
                x += 1
                y += 1
            
        # col
        for i in range(1, len(mat[0])):
            diag = []
            x, y = i, 0
            while 0 <= x < len(mat[0]) and 0 <= y < len(mat):
                diag.append(mat[y][x])
                x += 1
                y += 1
            
            diag.sort()
            x, y = i, 0
            while 0 <= x < len(mat[0]) and 0 <= y < len(mat):
                result[y][x] = diag[y]
                x += 1
                y += 1

        return result