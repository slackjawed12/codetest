class Solution:
    def repeatedCharacter(self, s: str) -> str:
        store = {}
        for c in s:
            if c not in store:
                store[c] = 1
            else:
                return c
        
        return 'a'