import sys

T = int(sys.stdin.readline().strip())


def input_data():
    a_size, b_size = list(map(int, sys.stdin.readline().strip().split()))
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    return [a, b]


result = []
for _ in range(T):
    a, b = input_data()
    a.sort()
    b.sort()
    j = 0
    count = 0
    for i, num in enumerate(a):
        while j < len(b) and num > b[j]:
            j += 1
        count += j

    result.append(count)

for r in result:
    print(r)