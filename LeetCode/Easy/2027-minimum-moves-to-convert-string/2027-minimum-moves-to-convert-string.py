class Solution:
    def minimumMoves(self, s: str) -> int:
        answer = 0
        i = 0
        while i < len(s):
            if s[i] == 'O':
                i += 1
                continue
            
            answer += 1
            i += 3
        
        return answer