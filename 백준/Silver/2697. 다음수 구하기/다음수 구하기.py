# 다음수 구하기
import sys

T = int(sys.stdin.readline().strip())
numbers = [sys.stdin.readline().strip() for _ in range(T)]


def get_next_number(n: str):
    cur, pos = n[-1], len(n) - 1
    while pos >= 0 and ord(n[pos]) >= ord(cur):
        cur = n[pos]
        pos -= 1

    if pos == -1:
        return "BIGGEST"

    tail, first_of_tail = list(n[pos:]), 0
    tail.sort()
    for i in range(len(tail)):
        if tail[i] > n[pos]:
            first_of_tail = tail[i]
            tail = tail[:i] + tail[i+1:]
            break

    return n[:pos] + first_of_tail + "".join(tail)


answer = []
for num in numbers:
    answer.append(get_next_number(num))

for a in answer:
    print(a)
