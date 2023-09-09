N = int(input())

cur = 1
result = 1
while cur <= N:
    temp = cur
    digit = temp % 10
    while (digit == 4 or digit == 7) and temp > 0:
        temp //= 10
        digit = temp % 10

    if temp == 0:
        result = cur

    cur += 1

print(result)
