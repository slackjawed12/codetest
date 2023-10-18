import sys

N, L = list(map(int, sys.stdin.readline().strip().split()))
input_signals = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
signals = {i[0]: i[1:] for i in input_signals}


def is_green_at(time, R, G):
    T = R + G
    if time % T < R:
        return False

    return True


cur, time = 0, 0
while cur < L:
    if cur not in signals:
        cur += 1
    else:
        R, G = signals[cur]
        cur += 1 if is_green_at(time, R, G) else 0
    time += 1

print(time)
