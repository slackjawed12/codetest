# 소수 사이 수열
import sys


class Solution:
    def __init__(self):
        self.board = [True] * 1299710
        self.init_board()

    def init_board(self):
        self.board[1] = False
        i = 2
        while i * i <= 1299710:
            if self.board[i]:
                for j in range(i * 2, 1299710, i):
                    self.board[j] = False

            i += 1

    def solve(self, n):
        return 0 if self.board[n] else self.get_series_length(n)

    def get_series_length(self, n):
        low = n
        while not self.board[low]:
            low -= 1

        high = n
        while not self.board[high]:
            high += 1

        return high - low


def main():
    t = int(sys.stdin.readline().strip())
    sol = Solution()
    answer = []
    for _ in range(t):
        num = int(sys.stdin.readline().strip())
        answer.append(sol.solve(num))

    for a in answer:
        print(a)


main()
