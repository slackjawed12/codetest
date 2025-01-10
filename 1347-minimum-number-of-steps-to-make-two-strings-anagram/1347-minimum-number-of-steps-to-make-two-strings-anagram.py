class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = defaultdict(int)
        for c in s:
            count_s[c] += 1
        
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        result = 0
        for k,v in count_s.items():
            if k not in count_t:
                result += v
            elif count_t[k] < v:
                result += v - count_t[k]
                
        return result
