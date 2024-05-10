class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        rotated_matrices = self.get_rotate(mat)
        for rot in rotated_matrices:
            if self.isEqual(rot, target):
                return True

        return False 

    def isEqual(self, mat1, mat2):
        for j in range(len(mat1)):
            for k in range(len(mat1[j])):
                if mat1[j][k] != mat2[j][k]:
                    return False
        
        return True
        
    def get_rotate(self, mat):
        result = [mat]
        for i in range(3):
            result.append(self.get_clockwise_rotate(result[-1]))

        return result

    def get_clockwise_rotate(self, mat):
        result = []
        for i in range(len(mat)):
            new_row = []
            for j in range(len(mat[i])):
                new_row.append(mat[j][len(mat)-i-1])
            
            result.append(new_row)
        
        return result