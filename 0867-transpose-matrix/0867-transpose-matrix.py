class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result =[]
        for i in range(len(matrix[0])):
            r = [row[i] for row in matrix]
            result.append(r)
        
        return result