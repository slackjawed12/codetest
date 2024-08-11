class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter = {}
        for c in word1:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        for c in word2:
            if c not in counter:
                counter[c] = -1
            else:
                counter[c] -= 1
        
        for v in counter.values():
            if abs(v) >= 4:
                return False

        return True