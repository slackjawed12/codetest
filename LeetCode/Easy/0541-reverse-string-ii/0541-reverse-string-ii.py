class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = ''
        length = len(s)
        for cnt, i in enumerate(range(0, length, k)):
            if cnt % 2:
                answer += s[:k]
            else:
                answer += s[k-1::-1]
            s = s[k:]
        return answer
        # abcdefghijklmnopqrstuvwxyzabcdefgh