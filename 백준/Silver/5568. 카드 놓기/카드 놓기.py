# 카드 놓기 - 순열
import sys


def input_variables():
    cards_numer = int(sys.stdin.readline().strip())
    choose_number = int(sys.stdin.readline().strip())
    cards_input = list(map(int, [sys.stdin.readline().strip() for _ in range(cards_numer)]))
    return [cards_numer, choose_number, *cards_input]


def permutation(arr, r):
    return permutation_helper(arr, r, [], [], [False]*len(arr))


def permutation_helper(arr, r, cur_arr, result, visit):
    if len(cur_arr) == r:
        result.append(cur_arr)
        return result

    for i in range(len(arr)):
        if visit[i] is False:
            copied_visit = list(visit)
            copied_visit[i] = True
            temp_arr = list(cur_arr)
            temp_arr.append(arr[i])
            result = permutation_helper(arr, r, temp_arr, result, copied_visit)

    return result


def concatenate_numbers(arr):
    result = ""
    for num in arr:
        result += str(num)

    return int(result)


n, k, *cards = input_variables()
permutations = permutation(cards, k)
answer = set([concatenate_numbers(per) for per in permutations])
print(len(answer))
