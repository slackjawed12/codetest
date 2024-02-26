# 접두사
import sys


class Solution:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())
        self.words = [sys.stdin.readline().strip() for _ in range(self.n)]

    def solve(self):
        sorted_words = sorted(self.words, reverse=True)
        answer = []
        for word in sorted_words:
            is_included = False
            for a in answer:
                if a.startswith(word):
                    is_included = True

            if not is_included:
                answer.append(word)

        return len(answer)


sol = Solution()
print(sol.solve())
