class Solution:
    def possibleStringCount(self, word: str) -> int:
        cur = ''
        result = 0
        for c in word:
            if c != cur:
                cur = c
            else:
                result += 1
        
        return result + 1
