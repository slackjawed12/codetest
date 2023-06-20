class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        answer = [[0]*c for _ in range(r)]
        x, y = 0, 0
        for i, row in enumerate(mat):
            for num in row:
                answer[y][x] = num
                if x == c-1:
                    x = 0
                    y += 1
                else:
                    x += 1
        
        return answer
        
        
            