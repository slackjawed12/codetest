class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        result = -1
        cur = startIndex
        dist = 0
        right_end = (startIndex-1)%len(words)
        while cur != right_end:
            if words[cur] == target:
                result = min(result, dist) if result != -1 else dist
                break
            
            dist += 1
            cur = (cur+1)%len(words)
        
        cur = startIndex
        dist = 0
        left_end = (startIndex+1)%len(words)
        while cur != left_end:
            if words[cur] == target:
                result = min(result, dist) if result != -1 else dist
                break
            
            dist += 1
            cur = (cur-1)%len(words)

        return result