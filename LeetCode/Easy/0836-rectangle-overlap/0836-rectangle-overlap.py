class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left, right = [rec1, rec2] if rec1[0] <= rec2[0] else [rec2, rec1]
        x_intersect = left[2] > right[0]
        if not x_intersect:
            return False

        low, high = [rec1, rec2] if rec1[1] <= rec2[1] else [rec2, rec1]
        y_intersect = low[3] > high[1]

        return y_intersect
