import sys
from itertools import chain

answer = []
while True:
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    if N == 0 and M == 0:
        break

    row_inputs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    ranks = list(chain(*row_inputs))
    ranks_counter = {}
    for rank in ranks:
        if rank not in ranks_counter:
            ranks_counter[rank] = 1
        else:
            ranks_counter[rank] += 1

    list_from_dict = list(ranks_counter.items())
    second_val = sorted(list(set(list(map(lambda x: x[1], list_from_dict)))), reverse=True)[1]
    seconds = [x[0] for x in list_from_dict if x[1] == second_val]
    answer.append(seconds)

for a in answer:
    print(*sorted(a))
