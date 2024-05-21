class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result = []
        for i in range(0,len(s), k):
            sliced = s[i:i+k]
            result.append(sliced)
        
        filled = fill*(k-len(result[-1]))
        result[-1] += filled
        return result