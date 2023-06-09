class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        end = -1
        for t in timeSeries:
            if t <= end:
                answer += t + duration - 1 - end
            else:
                answer += duration
                
            end = t + duration - 1
        
        return answer
                