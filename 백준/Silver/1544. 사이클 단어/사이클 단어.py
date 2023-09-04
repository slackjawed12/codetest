import sys

N = int(input())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())


def is_same_cycle(a: str, b: str):
    if len(a) != len(b):
        return False

    for i in range(len(b)):
        converted = a[i+1:]+a[0:i+1]
        if converted == b:
            return True

    return False


result = []
for word in words:
    if len(result) == 0:
        result.append(word)
    else:
        isSame = False
        for current in result:
            isSame = is_same_cycle(current, word)

            if isSame:
                break

        if not isSame:
            result.append(word)

print(len(result))
