def gcd(a, b) -> int:
    if a % b == 0:
        return b
    return gcd(b, a % b)


def lcm(a, b) -> int:
    g = gcd(a, b)
    return g * (a // g) * (b // g)


x, y, z, w = map(int, open(0).read().split())
deno = lcm(y, w)
num = x * deno // y + z * deno // w
divider = gcd(num, deno)

print(num//divider, deno//divider)
