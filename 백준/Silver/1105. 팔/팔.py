# 팔
import sys


class Solution:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def solve(self):
        left_list = list(str(self.left))
        right_list = list(str(self.right))
        if len(left_list) != len(right_list):
            return 0

        result = 0
        for i in range(len(left_list)):
            if left_list[i] == right_list[i]:
                if left_list[i] == '8':
                    result += 1
            else:
                break

        return result


def main():
    l, r = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution(l, r)
    answer = sol.solve()

    print(answer)


main()
