class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        result = [0]*m
        for i in range(m):
            cnt = 0
            current = [startPos[0], startPos[1]]
            for j in range(i, m):
                if s[j] == 'L':
                    current[1] -= 1
                elif s[j] == 'R':
                    current[1] += 1
                elif s[j] == 'U':
                    current[0] -= 1
                else:
                    current[0] += 1
                
                if 0 <= current[0] < n and 0 <= current[1] < n:
                    cnt += 1
                else:
                    break
            result[i] = cnt
        
        return result
                