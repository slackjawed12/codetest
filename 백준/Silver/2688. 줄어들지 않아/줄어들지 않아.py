# 줄어들지 않아
import sys


def input_data():
    t = int(sys.stdin.readline().strip())
    inputs = [int(sys.stdin.readline().strip()) for _ in range(t)]
    return inputs


def count_not_decreasing_numbers(n: int):
    start = [1] * 10
    for i in range(n):
        for digit in range(9, -1, -1):
            start[digit] += sum(start[:digit])

    return start[9]


def main():
    numbers = input_data()
    answer = [count_not_decreasing_numbers(n) for n in numbers]
    for a in answer:
        print(a)


main()
