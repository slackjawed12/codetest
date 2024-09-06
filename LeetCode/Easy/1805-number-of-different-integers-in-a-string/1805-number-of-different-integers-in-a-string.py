class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        digit = set(list('1234567890'))
        cur = -1
        result = set()
        for c in word:
            if c in digit:
                if cur == -1:
                    cur = int(c)
                else:
                    cur = cur*10 + int(c)
            else:
                if cur != -1:
                    result.add(cur)
                    cur = -1

        if cur != -1:
            result.add(cur)
            
        return len(result)