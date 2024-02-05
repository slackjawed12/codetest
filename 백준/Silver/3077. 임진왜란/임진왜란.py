import sys


def input_data():
    count = int(sys.stdin.readline().strip())
    first = list(sys.stdin.readline().strip().split())
    second = list(sys.stdin.readline().strip().split())
    return [count, first, second]


def get_score(origin: list, target: list):
    formatted = {name: i for i, name in enumerate(origin)}
    result = 0
    for i in range(len(target) - 1):
        for j in range(i, len(target)):
            if formatted[target[i]] < formatted[target[j]]:
                result += 1

    return str(result) + "/" + str(len(target) * (len(target) - 1) // 2)


N, battles, submit = input_data()
answer = get_score(battles, submit)
print(answer)
