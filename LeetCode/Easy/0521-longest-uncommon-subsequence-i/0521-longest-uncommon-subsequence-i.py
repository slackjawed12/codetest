from collections import Counter

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b) or a != b:
            return max(len(a), len(b))
        else:
            return -1