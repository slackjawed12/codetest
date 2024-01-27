# 사다리
import sys


def input_data():
    testcase = int(sys.stdin.readline().strip())
    numbers = []
    for _ in range(testcase):
        N = int(sys.stdin.readline().strip())
        numbers.append(list(map(int, sys.stdin.readline().strip().split())))
    return numbers


def get_minimum_ladder(target):
    init = [i for i in range(1, len(target) + 1)]
    temp = target[:]
    answer = 0
    for i in range(len(temp)):
        number = temp[0]
        idx = init.index(number)
        answer += abs(idx)
        temp = temp[1:]
        init = init[:idx] + init[idx + 1:]

    return answer


inputs = input_data()
answers = [get_minimum_ladder(i) for i in inputs]
for a in answers:
    print(a)
