class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = sum(travel) * 3 + sum(map(len,garbage))      
        for i in  "MPG":
            zipped = zip(garbage[::-1], travel[::-1])
            for g, t in zipped:
                if i in g: 
                    break
                time -= t
        return time