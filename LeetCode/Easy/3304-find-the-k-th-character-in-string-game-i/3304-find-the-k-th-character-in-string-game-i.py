class Solution:
    def kthCharacter(self, k: int) -> str:
        result = "a"
        while len(result) <= k:
            added = "".join([chr(ord('a')+(ord(c)-ord('a')+1)%26) for c in result])
            result += added
        
        return result[k-1]