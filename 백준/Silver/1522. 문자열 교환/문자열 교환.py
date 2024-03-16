import sys


class Solution:
    def __init__(self, string: str):
        self.string = string

    def solve(self):
        count = len([c for c in self.string if c == 'a'])
        answer = 9999
        for i in range(len(self.string)):
            sliced = self.string[i:(i + count)]
            sliced += self.string[0:count-len(sliced)]
            change_count = len([c for c in sliced if c == 'b'])
            answer = min(answer, change_count)

        return answer


def main():
    string = sys.stdin.readline().strip()
    sol = Solution(string)
    answer = sol.solve()
    print(answer)


if __name__ == '__main__':
    main()
