class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result = []
        for i, r in enumerate(grid):
            if i %2 == 0:
                result += [n for j, n in enumerate(r) if j%2==0] 
            else:
                result += list(reversed([n for j, n in enumerate(r) if j%2!=0]))
        
        return result
            