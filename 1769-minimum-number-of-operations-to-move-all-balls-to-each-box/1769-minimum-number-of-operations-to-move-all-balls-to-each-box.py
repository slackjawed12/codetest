class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            cur = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    cur += abs(i-j)
            
            result.append(cur)
    
        return result
            
                