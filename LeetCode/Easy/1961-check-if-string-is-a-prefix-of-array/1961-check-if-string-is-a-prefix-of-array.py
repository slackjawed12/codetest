class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        pos = 0
        low, high = 0, 0
        for word in words:
            low, high = pos, pos + len(word)
            if low >= len(s):
                break

            sub = s[low:high]
            if sub != word:
                return False

            pos = high
        
        low, high = pos, pos + len(word)
        return low >= len(s)