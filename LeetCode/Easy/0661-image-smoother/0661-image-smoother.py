class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        temp = [row[:] for row in img]
        dx = [-1,0,1,-1,0,1,-1,0,1]
        dy = [-1,-1,-1,0,0,0,1,1,1]
        for i in range(len(img)):
            for j in range(len(img[i])):
                cell_sum, count = 0, 0
                for k in range(9):
                    x, y = j+dx[k], i+dy[k]
                    if 0<=x<len(img[i]) and 0<=y<len(img):
                        count += 1
                        cell_sum += img[y][x]
                        
                temp[i][j] = cell_sum//count

        return temp
