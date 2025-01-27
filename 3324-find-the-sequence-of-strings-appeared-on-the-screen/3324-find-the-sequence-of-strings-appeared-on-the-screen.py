class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = ['a']
        while result[-1] != target:
            last = result[-1]
            if target[len(last)-1] != last[-1]:
                result.append(self.key2(last))
            else:
                result.append(self.key1(last))

        return result
    
    def key1(self, s:str) -> str:
        return s + "a"
    
    def key2(self, s:str) -> str:
        if s:
            last= s[-1]
            n = (ord(last)-ord('a')+1)%26
            return s[:-1]+chr(n+ord('a'))

        return s