class Solution:
    def scoreOfString(self, s: str) -> int:
        answer = 0
        for i, c in enumerate(s[:-1]):
            answer += abs(ord(c)-ord(s[i+1]))

        return answer