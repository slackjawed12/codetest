import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))
weights = list(map(int, sys.stdin.readline().strip().split()))


def get_total(arr, K):
    return get_total_helper(arr, K, 0, 500, [], [False] * len(arr))


def get_total_helper(arr, K, result, cur_weight, cur_routine, visit):
    if cur_weight < 500:
        return 0
    elif len(cur_routine) == len(arr):
        result += 1
        return result

    r = result
    for i, w in enumerate(arr):
        if not visit[i]:
            visit[i] = True
            cur_routine.append(i)
            r += get_total_helper(arr, K, result, cur_weight - K + w, cur_routine, visit)
            visit[i] = False
            cur_routine.pop()

    return r


print(get_total(weights, K))
