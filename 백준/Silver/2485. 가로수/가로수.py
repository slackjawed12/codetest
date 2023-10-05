import sys

N = int(sys.stdin.readline().strip())


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


trees = [int(sys.stdin.readline().strip()) for _ in range(N)]
diff = [trees[i + 1] - trees[i] for i in range(len(trees) - 1)]
diff_gcd = 0

for i in range(len(diff)):
    diff_gcd = gcd(diff[i], diff_gcd)

result = 0
for d in diff:
    result += (d // diff_gcd) - 1

print(result)
