# 비밀편지 : 2차원 배열에서 시계방향 회전 결과 구현
import sys

T = int(input())
cases = [sys.stdin.readline().strip() for _ in range(T)]


def rotate_string_clockwise(target):
    row = 1
    while row * row < len(target):
        row += 1

    temp = ["".join(target[i * row:(i + 1) * row]) for i in range(row)]
    result = []

    for i in reversed(range(row)):
        a_string = "".join([sliced[i] for sliced in temp])
        result.append("".join(a_string))

    return "".join(result)


out = [rotate_string_clockwise(message) for message in cases]

print("\n".join(out))
