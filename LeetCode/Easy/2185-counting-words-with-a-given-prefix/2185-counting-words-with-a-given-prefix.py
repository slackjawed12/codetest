class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        return sum([1 if self.startsWith(word, pref) else 0 for word in words])
    
    def startsWith(self, target, prefix):
        if len(prefix) > len(target):
            return False

        return target[:len(prefix)] == prefix
            