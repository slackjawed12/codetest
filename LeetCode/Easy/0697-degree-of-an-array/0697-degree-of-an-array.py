from typing import List
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [i]
            else:
                d[n].append(i)
        
        deg = max([len(v) for v in d.values()])
        result = 99999
        for k,v in d.items():
            if len(v) == deg:
                diff = v[-1] - v[0] + 1
                result = min(diff, result)
        
        return result
        