class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            a = "".join(sorted(s))
            if a in result:
                result[a].append(s)
            else:
                result[a] = [s]
        
        return list(result.values())