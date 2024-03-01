# 나이트의 이동
import sys
from collections import deque


class Solution:
    def __init__(self, length, start, end):
        self.length = length
        self.start = start
        self.end = end

    def solve(self):
        board = [[-1] * self.length for _ in range(self.length)]
        move_dir = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
        cur = self.start
        q = deque([])
        q.append([cur[0], cur[1], 0])
        board[self.start[1]][self.start[0]] = 0
        dist = 1
        while len(q) > 0:
            cur = q.popleft()

            for i in range(8):
                nx, ny, next_dist = cur[0] + move_dir[i][0], cur[1] + move_dir[i][1], cur[2]+1
                if 0 <= nx < self.length and 0 <= ny < self.length:
                    if board[ny][nx] == -1:
                        q.append([nx, ny, next_dist])
                        board[ny][nx] = next_dist

            dist += 1

        return board[self.end[1]][self.end[0]]


def main():
    t = int(sys.stdin.readline().strip())
    answer = []
    for _ in range(t):
        length = int(sys.stdin.readline().strip())
        start = list(map(int, sys.stdin.readline().strip().split()))
        end = list(map(int, sys.stdin.readline().strip().split()))
        sol = Solution(length, start, end)
        answer.append(sol.solve())

    for a in answer:
        print(a)


main()
