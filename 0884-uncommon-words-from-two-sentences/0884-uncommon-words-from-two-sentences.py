class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = defaultdict(int)
        for word in (s1 + " " + s2).split():
            d[word] += 1

        return [k for k,v in d.items() if v == 1]