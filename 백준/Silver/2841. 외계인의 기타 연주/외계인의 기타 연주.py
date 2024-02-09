# 2841 외계인의 기타 연주
import sys


def main():
    N, P, melodies = input_data()
    answer = get_min_moving(melodies, P)
    print(answer)


def input_data():
    N, P = list(map(int, sys.stdin.readline().strip().split()))
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    return [N, P, arr]


def get_min_moving(melodies: list[list], P: int):
    info = {i: [] for i in range(1, 7)}
    count = 0
    for melody in melodies:
        line, pret = melody
        current_press = info[line]
        while len(current_press) > 0 and current_press[-1] > pret:
            current_press.pop()
            count += 1

        if len(current_press) > 0 and current_press[-1] == pret:
            continue

        current_press.append(pret)
        count += 1

    return count


main()
