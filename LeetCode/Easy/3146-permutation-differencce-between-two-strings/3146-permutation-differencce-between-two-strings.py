class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        store = {c:i for i,c in enumerate(s)}
        result = 0
        for i, c in enumerate(t):
            result += abs(store[c]-i)
        
        return result