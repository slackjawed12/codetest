class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        answer =  0
        for s in strs:
            try:
                answer = max(answer, int(s))
            except Exception as e:
                answer = max(answer,len(s))
        
        return answer