import sys

N = int(sys.stdin.readline().strip())
time_table = [sys.stdin.readline().strip().split() for _ in range(N)]


def conversion_time(str):
    hour_time = int(str[0:2]) * 60
    min_time = int(str[2:])
    return hour_time + min_time


time_info = [[conversion_time(t[0]), conversion_time(t[1])] for t in time_table]
START_TIME = 10 * 60
END_TIME = 22 * 60
occupation = [0] * (END_TIME + 1)
for time in time_info:
    for n in range(time[0] - 10, min(END_TIME + 1, time[1] + 10)):
        occupation[n] = 1

answer = 0
flag = True
cnt = 0
for i in occupation[START_TIME:-1]:
    if i == 0:
        if not flag:  # one to zero
            flag = True
        cnt = cnt + 1
    else:  # i == 1
        if flag:
            cnt = 0
            flag = False
    answer = max(answer, cnt)

print(answer)
