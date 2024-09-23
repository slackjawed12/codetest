from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image

        q = deque([(sc, sr)])
        d = [(0,-1),(-1,0),(1,0),(0,1)]
        start = image[sr][sc]
        while q:
            x, y = q.popleft()
            image[y][x] = color
            for dx, dy in d:
                if 0 <= x+dx < len(image[0]) and 0 <= y+dy < len(image):
                    if image[y+dy][x+dx] == start:
                        q.append((x+dx, y+dy))
    
        return image