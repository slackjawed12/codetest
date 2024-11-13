class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for y in range(len(matrix)//2):
            l = len(matrix[0]) - 2 * y
            for x in range(y, y + l-1):
                dx, dy = l-1-(x-y), x-y
                temps = [matrix[y][x], matrix[y+dy][x+dx], matrix[y+dy+dx][x+dx-dy], matrix[y+dx][x-dy]]
                matrix[y+dy][x+dx] = temps[0]
                matrix[y+dy+dx][x+dx-dy] = temps[1]
                matrix[y+dx][x-dy] = temps[2]
                matrix[y][x] = temps[3]