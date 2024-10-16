class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start, end = 0, 0
        cur = s[0] 

        for i in range(1,len(s)):
            if s[i] == cur:
                end += 1
            else:
                if end-start >= 2:
                    result.append([start,end])
                start,end =i,i
                cur = s[i]
        
        return result
                
            
            