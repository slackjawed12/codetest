import sys
T = int(sys.stdin.readline().strip())


def all_different_mod(numbers):
    i = 1
    while True:
        keys = {}
        for num in numbers:
            keys[num % i] = num

        if len(keys) == len(numbers):
            print(i)
            break

        i += 1


result = []
for _ in range(T):
    G = int(sys.stdin.readline().strip())
    nums = [int(sys.stdin.readline().strip()) for _ in range(G)]

    all_different_mod(nums)

