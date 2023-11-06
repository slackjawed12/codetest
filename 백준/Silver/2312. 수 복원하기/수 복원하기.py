import sys

T = int(sys.stdin.readline().strip())
inputs = [int(sys.stdin.readline().strip()) for _ in range(T)]


def is_prime(i):
    if i == 1:
        return False
    if i == 2:
        return True
    for j in range(2, i):
        if j * j > i:
            break
        if i % j == 0:
            return False

    return True


result = []
for num in inputs:
    temp = num
    i = 2
    while temp != 1:
        if is_prime(i):
            count = 0
            while temp % i == 0:
                count += 1
                temp = temp // i

            if count > 0:
                result.append(" ".join([str(i), str(count)]))
        i += 1

print("\n".join(result))
