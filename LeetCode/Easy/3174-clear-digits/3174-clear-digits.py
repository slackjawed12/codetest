class Solution:
    def clearDigits(self, s: str) -> str:
        result = s
        digits = set('0123456789')
        while True:
            i = 0
            
            while i < len(result) and result[i] not in digits:
                i += 1
            
            if i == len(result):
                break
            
            j = i-1
            while j >= 0 and result[j] in digits:
                j -= 1

            result = result[:j]+result[j+1:i]+result[i+1:]

        return result

# stack
class Solution2:
    def clearDigits(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                res.pop()
            else:
                res.append(s[i])
        return ''.join(res)