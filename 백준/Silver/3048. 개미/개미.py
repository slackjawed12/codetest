# 개미
import sys

N1, N2 = list(map(int, sys.stdin.readline().strip().split()))
first_input = sys.stdin.readline().strip()
second_input = sys.stdin.readline().strip()
T = int(sys.stdin.readline().strip())

first = list(map(lambda x: [x, 1], first_input))
second = list(map(lambda x: [x, -1], second_input))

cur_order = list(reversed(first)) + second
cur_time = 0
while cur_time < T:
    i = 0
    while i < len(cur_order) - 1:
        if cur_order[i + 1][1] == -1 and cur_order[i][1] == 1:
            temp_right = cur_order[i + 1]
            temp_left = cur_order[i]
            cur_order[i] = temp_right
            cur_order[i + 1] = temp_left
            i += 2
        else:
            i += 1

    cur_time += 1

print("".join(list(map(lambda x: x[0], cur_order))))
