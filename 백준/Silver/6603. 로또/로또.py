import sys


def combination(array, count):
    return combination_helper(array, count, -1, [], [])


def combination_helper(array, count, cur_index, cur_store, result):
    if len(cur_store) == count:
        result.append(cur_store[:])
        return result

    for i in range(cur_index + 1, len(array)):
        cur_store.append(array[i])
        result = combination_helper(array, count, i, cur_store, result)
        cur_store.pop()

    return result


answers = []
while True:
    testcase = list(map(int, sys.stdin.readline().strip().split()))
    if testcase[0] == 0:
        break

    numbers = testcase[1:]
    answers.append(combination(numbers, 6))


for answer in answers:
    for combi in answer:
        print(*combi)

    print()