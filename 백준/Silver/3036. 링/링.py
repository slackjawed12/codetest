import sys

N = int(sys.stdin.readline().strip())
first, *targets = list(map(int, sys.stdin.readline().strip().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def get_expr(a, b):
    top = a
    bottom = b
    cur_gcd = gcd(top, bottom)
    while cur_gcd != 1:
        top //= cur_gcd
        bottom //= cur_gcd
        cur_gcd = gcd(top, bottom)

    return str(top) + "/" + str(bottom)


result = [get_expr(first, ring) for ring in targets]
print("\n".join(result))
