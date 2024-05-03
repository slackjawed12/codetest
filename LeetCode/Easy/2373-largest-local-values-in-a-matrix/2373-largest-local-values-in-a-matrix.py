class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        answer =[]
        for i in range(len(grid)-2):
            new_row = []
            for j in range(len(grid[i])-2):
                cell_max = max([max(row[j:j+3])for row in grid[i:i+3]])
                new_row.append(cell_max)

            answer.append(new_row)
        
        return answer
