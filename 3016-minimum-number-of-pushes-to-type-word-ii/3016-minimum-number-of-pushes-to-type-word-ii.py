class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1
        
        temp = list(freq.items())
        temp.sort(key=lambda x:-x[1])

        result = 0
        for i, data in enumerate(temp):
            k, v = data
            if i < 8:
                result += 1 * v
            elif i < 16:
                result += 2 * v
            elif i < 24:
                result += 3 * v
            else:
                result += 4 * v

        return result