import sys

X = int(sys.stdin.readline().strip())

number = list(str(X))


def permutation(arr, r):
    return permutation_helper(arr, r, [], [], [False] * len(arr))


def permutation_helper(source, r, cur_arr, result, visit):
    if len(cur_arr) == r:
        result.append(cur_arr.copy())
        return result

    for index, e in enumerate(source):
        if not visit[index]:
            visit[index] = True
            cur_arr.append(e)
            permutation_helper(source, r, cur_arr, result, visit)
            visit[index] = False
            cur_arr.pop()

    return result


permutations = list(map(lambda x: int("".join(x)), permutation(number, len(number))))
greater_than = [n for n in permutations if n > X]
answer = min(greater_than) if len(greater_than) > 0 else 0
print(answer)
