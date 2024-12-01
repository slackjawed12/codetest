class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        group = [[] for i in range(n+1)]
        for person, volume in enumerate(groupSizes):
            cur = group[volume]
            is_set = False
            for chunk in cur:
                if len(chunk) < volume:
                    is_set = True
                    chunk.append(person)
                    break
            
            if not is_set:
                cur.append([person])
        
        result = []
        for g in group:
            if len(g) != 0:
                for chunk in g:
                    result.append(chunk)
            
        return result
        