class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = []
        for row in range(numRows):
            cur = row
            while cur < len(s):
                result += s[cur]
                nxt = cur + 2 * numRows - 2
                mid = nxt - 2 * row
                if cur < mid < nxt and mid < len(s):
                    result += s[mid]

                cur = nxt
        

        return "".join(result)