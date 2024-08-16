class Solution:
    def reformat(self, s: str) -> str:
        digits = [c for c in s if ord(c) >= ord('0') and ord(c) <= ord('9')]
        letters = [c for c in s if ord(c) >= ord('a') and ord(c) <= ord('z')]

        if abs(len(digits) - len(letters)) >= 2:
            return ""

        result = [] 
        longer, shorter = [digits, letters] if len(digits) >= len(letters) else [letters, digits]
        result = self.crossadd(longer, shorter)

        return "".join(result)

    def crossadd(self, longer, shorter):
        result = []
        i = 0
        while i < len(shorter):
            result.append(longer[i])
            result.append(shorter[i])
            i += 1
        
        if len(longer) != len(shorter):
            result.append(longer[i])
        
        return result