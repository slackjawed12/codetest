class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return "".join([s[(i+k)%len(s)] for i, c in enumerate(s)])