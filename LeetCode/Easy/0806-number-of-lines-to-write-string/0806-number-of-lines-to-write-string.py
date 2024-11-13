class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = [0,0]
        line = 0
        for c in s:
            width = widths[ord(c)-ord('a')]
            if line+width > 100:
                result[0] += 1
                line = width
            else:
                line += width
        
        if line:
            result[0] += 1

        result[1] = line
        return result