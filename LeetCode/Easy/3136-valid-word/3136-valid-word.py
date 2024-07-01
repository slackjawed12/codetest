class Solution:
    def isValid(self, word: str) -> bool:
        s = set(word)
        a = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        v = set('aeiouAEIOU')
        if len(word) < 3:
            return False
        
        if set('@#$') & s:
            return False
        
        if not (v & s):
            return False
        
        if not (a-v & s):
            return False
        
        return True