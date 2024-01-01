# 차이를 최대로
import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))


def permutation(array, count):
    return permutation_helper(array, count, [], [], [False] * len(array))


def permutation_helper(array, count, cur_store, result, visit):
    if len(cur_store) == count:
        result.append(cur_store[:])
        return result

    for index, num in enumerate(array):
        if not visit[index]:
            visit[index] = True
            cur_store.append(num)
            result = permutation_helper(array, count, cur_store, result, visit)
            visit[index] = False
            cur_store.pop()

    return result


perm = permutation(nums, len(nums))
answer = 0
for arr in perm:
    temp = 0
    for i in range(len(arr) - 1):
        temp += abs(arr[i] - arr[i + 1])

    answer = max(temp, answer)

print(answer)
