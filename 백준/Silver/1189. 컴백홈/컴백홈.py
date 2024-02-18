import sys


class Solution:
    def __init__(self):
        self.row, self.col, self.distance = list(map(int, sys.stdin.readline().strip().split()))
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, -1, 0, 1]
        self.board = [list(sys.stdin.readline().strip()) for _ in range(self.row)]

    def search(self):
        trace = [(0, self.row - 1)]
        visit = [[False] * self.col for _ in range(self.row)]
        visit[self.row - 1][0] = True
        return self.search_helper(trace, visit, 0)

    def search_helper(self, trace: list, visit: list, result: int):
        if trace[-1][0] == self.col - 1 and trace[-1][1] == 0 and len(trace) == self.distance:
            return result + 1
        elif trace[-1][0] == self.col - 1 and trace[-1][1] == 0:
            return result
        elif len(trace) == self.distance:
            return result

        for i in range(4):
            nx, ny = trace[-1][0] + self.dx[i], trace[-1][1] + self.dy[i]
            if 0 <= nx < self.col and 0 <= ny < self.row and not visit[ny][nx]:
                visit[ny][nx] = True
                if self.board[ny][nx] == '.':
                    trace.append((nx, ny))
                    result = self.search_helper(trace, visit, result)
                    trace.pop()
                    visit[ny][nx] = False

        return result


sol = Solution()
print(sol.search())
