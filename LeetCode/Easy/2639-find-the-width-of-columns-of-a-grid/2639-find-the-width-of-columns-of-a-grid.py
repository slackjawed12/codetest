class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        answer = []
        for c in range(len(grid[0])):
            max_len= 0
            for r in range(len(grid)):
                num = grid[r][c]
                max_len = max(len(str(num)), max_len)
            
            answer.append(max_len)
        
        return answer