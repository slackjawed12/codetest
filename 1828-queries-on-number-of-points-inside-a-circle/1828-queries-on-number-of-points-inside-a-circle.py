class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for query in queries:
            xc, yc, r = query
            cnt = 0
            for point in points:
                x, y = point
                d_square = (xc-x) * (xc-x) + (yc-y) * (yc-y)
                if r * r >= d_square:
                    cnt += 1
            
            result.append(cnt)
        
        return result
                    