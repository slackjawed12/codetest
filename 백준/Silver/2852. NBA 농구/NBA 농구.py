import sys

N = int(sys.stdin.readline().strip())
score_info = [sys.stdin.readline().strip().split() for _ in range(N)]


def add_leading_zero(num):
    return str(num) if num >= 10 else '0' + str(num)


cur_time, score_a, score_b = 0, 0, 0
time_dict = {'draw': 0, 'a_win': 0, "b_win": 0}
cur_state = 'draw'
basketball_second = 48 * 60
for info in score_info:
    team = int(info[0])
    score_minute, score_second = list(map(int, info[1].split(":")))
    total_second = score_minute * 60 + score_second - cur_time
    time_dict[cur_state] += total_second
    if team == 1:
        score_a += 1
    else:
        score_b += 1

    if score_a > score_b:
        cur_state = 'a_win'
    elif score_b > score_a:
        cur_state = 'b_win'
    else:
        cur_state = 'draw'

    cur_time = score_minute * 60 + score_second

recorded_time = basketball_second - sum(list(time_dict.values()))
time_dict[cur_state] += recorded_time

hour_a, min_a = time_dict['a_win'] // 60, time_dict['a_win'] % 60
hour_b, min_b = time_dict['b_win'] // 60, time_dict['b_win'] % 60

print(add_leading_zero(hour_a) + ":" + add_leading_zero(min_a))
print(add_leading_zero(hour_b) + ":" + add_leading_zero(min_b))
