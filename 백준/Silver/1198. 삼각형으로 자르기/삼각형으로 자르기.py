import sys


def area(a, b, c):
    vector_one = (a[0] - b[0], a[1] - b[1])
    vector_two = (a[0] - c[0], a[1] - c[1])
    det = vector_one[0] * vector_two[1] - vector_one[1] * vector_two[0]
    return abs(det / 2)


def combination(arr, r):
    return combination_helper(arr, r, -1, [], [])


def combination_helper(arr, choose_count, cur_pos, cur_store, result):
    if len(cur_store) == choose_count:
        result.append(cur_store[:])
        return result

    for next_pos in range(cur_pos + 1, len(arr)):
        cur_store.append(arr[next_pos])
        result = combination_helper(arr, choose_count, next_pos, cur_store, result)
        cur_store.pop()

    return result


N = int(sys.stdin.readline().strip())
points = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
all_combinations = combination(points, 3)
all_possible_area = [area(combi[0], combi[1], combi[2]) for combi in all_combinations]

print(max(all_possible_area))
