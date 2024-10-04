from typing import List
from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = []
        for word in words:
            di = defaultdict(int)
            for c in word:
                di[c] += 1

            counts.append(di)

        result =[]
        for a in set('abcdefghijklmnopqrstuvwxyz'):
            common_freq = min([cnt[a] if a in cnt else 0 for cnt in counts])
            result += [a]*common_freq
            
        return result