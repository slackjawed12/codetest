class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        p = [i+1 for i in range(m)]
        for q in queries:
            for i in range(m):
                if p[i] == q:
                    result.append(i)
                    p = [q] + p[:i]+p[i+1:]
                    break
        
        return result