from collections import Counter
from math import floor
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        counts = Counter(s)
        return floor(counts[letter]/len(s)*100)