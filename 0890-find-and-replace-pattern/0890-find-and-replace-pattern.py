class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words if self.matchPattern(word, pattern)]
                
    def matchPattern(self, word, pattern):
        fun = {}
        inv = {}
        for i in range(len(word)):
            x, y = word[i], pattern[i]
            if x not in fun:
                if y in inv:
                    return False
                fun[x] = y
                inv[y] = x
            else:
                if y not in inv:
                    return False
                elif fun[x] != y or inv[y] != x:
                    return False
        
        return True
        
        