import sys

T = int(sys.stdin.readline().strip())
number_inputs = [int(sys.stdin.readline().strip()) for _ in range(T)]


def five_multiples(num):
    count = 0
    while num != 0:
        multi = num // 5
        count += multi
        num = multi

    return count


result = [five_multiples(num) for num in number_inputs]
for ans in result:
    print(ans)