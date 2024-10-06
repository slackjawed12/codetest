import sys
from typing import List


def input_data():
    N = sys.stdin.readline().strip()
    first = list(map(int, sys.stdin.readline().strip().split()))
    M = sys.stdin.readline().strip()
    second = list(map(int, sys.stdin.readline().strip().split()))
    return [first, second]


def solve(cards: List[int], target: List[int]) -> List[int]:
    s = set(cards)
    result = [1 if n in s else 0 for n in target]
    return result


def output_answer(answer: List[int]):
    print(*answer)


f_arr, s_arr = input_data()
ans = solve(f_arr, s_arr)
output_answer(ans)
