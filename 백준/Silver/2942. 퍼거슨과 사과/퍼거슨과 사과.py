import sys

R, G = list(map(int, sys.stdin.readline().strip().split()))


def get_all_common_divisor(a, b):
    i = 1
    big, small = max(a, b), min(a, b)
    divisor = []
    while i * i <= big:
        if big % i == 0:
            divisor.append(i)
            divisor.append(big // i)
        i += 1

    answer = []
    for d in divisor:
        if small % d == 0:
            answer.append(d)

    return answer


common_divisors = get_all_common_divisor(R, G)
for divisor in common_divisors:
    print(divisor, R // divisor, G // divisor)
