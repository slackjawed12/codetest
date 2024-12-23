class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        left_moves = [0] * n
        left = int(boxes[0])
        for i in range(1, n):
            left_moves[i] = left_moves[i-1] + left
            if boxes[i] == '1':
                left += 1
        
        right_moves = [0]*n
        right = int(boxes[-1])
        for i in range(1, n):
            right_moves[-1-i] = right_moves[-1-i+1] + right
            if boxes[-1-i] == '1':
                right += 1

        return [l + r for l, r in zip(left_moves, right_moves)]