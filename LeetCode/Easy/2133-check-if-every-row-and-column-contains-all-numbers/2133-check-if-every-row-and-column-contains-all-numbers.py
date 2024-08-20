class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        s = set(range(1,n+1))

        # row
        for i in range(n):
            r, c = set(matrix[i]), set([row[i] for row in matrix])
            if r != s or c != s:
                return False

        return True        
