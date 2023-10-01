# K-세준수 : 소인수 중 최댓값이 K보다 크지 않은 수를 N 이하 자연수에서 찾기
N, K = int(input()), int(input())


def is_prime(num):
    if num == 1:
        return False

    x = 2
    while x * x <= num:
        if num % x == 0:
            return False
        x += 1

    return True


result = 1
primes = {n for n in range(2, K + 1) if is_prime(n) is True}

factor = [[i] if i in primes else [] for i in range(N + 1)]
for i in range(2, N + 1):
    flag = False
    for p in primes:
        if i % p == 0:
            flag = True
            factor[i] = factor[p] + factor[i // p]
            break

    if flag is False:
        factor[i] = [i]

for f in factor:
    if len(f) == 0:
        continue
    if max(f) <= K:
        result += 1

print(result)
