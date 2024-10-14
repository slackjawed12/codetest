# 빙고
import sys
from typing import List


class Solution:
    def solve(self, board: List[List[int]], call: List[List[int]]) -> int:
        flat_call = sum(call, [])
        cur = [[False] * 5 for _ in range(5)]
        res = 0
        for i, n in enumerate(flat_call):
            self.update_board(n, board, cur)

            if self.is_bingo(cur):
                res = i + 1
                break

        return res

    def update_board(self, n, board, info: List[List[bool]]):
        for y, row in enumerate(board):
            for x, number in enumerate(row):
                if number == n:
                    info[y][x] = True

        return

    def is_bingo(self, info: List[List[bool]]) -> bool:
        row = self.count_row(info)
        col = self.count_col(info)
        diag = self.count_diagonal(info)
        return row + col + diag >= 3

    def count_row(self, info: List[List[bool]]) -> int:
        result = 0
        for r in info:
            if r.count(True) == len(r):
                result += 1

        return result

    def count_col(self, info: List[List[bool]]) -> int:
        result = 0
        for i in range(len(info[0])):
            temp = 0
            for j in range(len(info)):
                if info[j][i]:
                    temp += 1

            if temp == len(info[0]):
                result += 1

        return result

    def count_diagonal(self, info: List[List[bool]]) -> int:
        result = 0
        dec = 0
        for i in range(len(info)):
            if info[i][i]:
                dec += 1

        if dec == len(info):
            result += 1

        inc = 0
        for j in range(len(info)):
            if info[j][len(info) - j - 1]:
                inc += 1

        if inc == len(info):
            result += 1

        return result


def main():
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
    call = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
    sol = Solution()
    answer = sol.solve(board, call)
    print(answer)


if __name__ == '__main__':
    main()
