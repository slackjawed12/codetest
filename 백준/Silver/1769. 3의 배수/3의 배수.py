X = input()

count, isThree = 0, "NO"
while True:
    if len(X) == 1:
        isThree = "YES" if (int(X) % 3) == 0 else "NO"
        break
    temp = list(X)
    total = sum(map(int, temp))
    count += 1
    X = str(total)

answer = list(map(str, [count, isThree]))
print('\n'.join(answer))
