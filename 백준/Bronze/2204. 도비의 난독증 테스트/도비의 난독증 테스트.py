# 도비의 난독증 테스트
import sys
from typing import List


class Solution:
    def solve(self, words: List[str]) -> str:
        result = None
        for word in words:
            if result is None:
                result = word
            else:
                lw = word.lower()
                lr = result.lower()
                m = min(lw, lr)
                result = result if m == lr else word

        return result


def main():
    answers = []
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break

        arr = [sys.stdin.readline().strip() for _ in range(n)]
        sol = Solution()
        answers.append(sol.solve(arr))

    for a in answers:
        print(a)


if __name__ == '__main__':
    main()
