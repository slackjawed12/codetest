import sys


def get_duplicated_combi(nums, m):
    return get_duplicated_combi_helper(nums, m, [], [])


def get_duplicated_combi_helper(arr, count, cur_store, result):
    if len(cur_store) == count:
        result.append(cur_store[:])
        return result

    for n in arr:
        cur_store.append(n)
        result = get_duplicated_combi_helper(arr, count, cur_store, result)
        cur_store.pop()

    return result


N, M = list(map(int, sys.stdin.readline().strip().split()))
nums = list(map(int, sys.stdin.readline().strip().split()))
listed_set_nums = list(set(nums))
listed_set_nums.sort()
answer = get_duplicated_combi(listed_set_nums, M)

for arr in answer:
    print(*arr)
