import sys
from collections import deque


def main():
    N, symbols = input_data()
    max_ans, min_ans = get_max_min_pair(symbols)
    print(max_ans)
    print(min_ans)


def input_data():
    N = int(sys.stdin.readline().strip())
    symbols = sys.stdin.readline().strip().split()
    return [N, symbols]


def get_max_min_pair(symbol_list: list):
    length = len(symbol_list)
    max_number = deque([str(9 - i) for i in range(length + 1)])
    min_number = deque([str(i) for i in range(length + 1)])
    max_stack, min_stack = [], []
    max_temp, min_temp = [], []
    for i, sym in enumerate(symbol_list):
        max_temp.append(max_number.popleft())
        min_temp.append(min_number.popleft())
        if sym == '<':
            while len(min_temp) > 0:
                min_stack.append(min_temp.pop())
        else:
            while len(max_temp) > 0:
                max_stack.append(max_temp.pop())

    max_temp.append(max_number.popleft())
    min_temp.append(min_number.popleft())
    while len(max_temp) > 0:
        max_stack.append(max_temp.pop())
    while len(min_temp) > 0:
        min_stack.append(min_temp.pop())

    return ["".join(max_stack), "".join(min_stack)]


main()
