import sys
from functools import cmp_to_key


def input_data():
    count = int(sys.stdin.readline().strip())
    infos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(count)]
    return count, infos


def cmp(x, y):
    first = x['power'] + x['ring'] * y['power']
    second = y['power'] + y['ring'] * x['power']
    return second - first


def get_min_cost_array(info_arr: list):
    table = [{"power": info_arr[i][0], "ring": info_arr[i][1], "index": i} for i in range(len(info_arr))]
    table.sort(key=cmp_to_key(cmp))
    return [t['index'] + 1 for t in table]


N, info = input_data()
answer = get_min_cost_array(info)

for a in answer:
    print(a)
