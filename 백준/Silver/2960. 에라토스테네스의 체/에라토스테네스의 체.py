import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))


def erato(target, cnt):
    count = 0
    answer = 0
    arr = [False] * (target + 1)
    find_cnt = False
    for i in range(2, N + 1):
        if arr[i] is False:
            for j in range(i, N+1, i):
                if arr[j] is False:
                    arr[j] = True
                    count += 1

                if count == cnt:
                    answer = j
                    find_cnt = True
                    break

        if find_cnt is True:
            break

    return answer


print(erato(N, K))
