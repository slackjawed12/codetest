# 금민수의 개수
import sys


class Solution:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def solve(self):
        numbers = [4, 7]
        i = 0
        while numbers[-1] < self.right:
            numbers.append(numbers[i] * 10 + 4)
            numbers.append(numbers[i] * 10 + 7)
            i += 1

        start = 0
        while numbers[start] < self.left:
            start += 1

        end = 0
        while numbers[end] < self.right:
            end += 1

        if numbers[end] != self.right:
            end -= 1

        return end - start + 1


def main():
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution(a, b)
    answer = sol.solve()
    print(answer)


if __name__ == '__main__':
    main()
