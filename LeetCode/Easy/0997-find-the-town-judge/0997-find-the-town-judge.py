class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {0:set(range(1,n+1))}
        for u,v in trust:
            d[0].discard(u)
            if u not in d:
                d[u] = set([v])
            else:
                d[u].add(v)
        
        if len(d[0]) != 1:
            return -1
        
        candidate = list(d[0])[0]
        for k, v in d.items():
            if candidate not in v:
                return -1
            
        return candidate