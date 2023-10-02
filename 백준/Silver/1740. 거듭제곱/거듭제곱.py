N = int(input())

digit = 1
answer = 0
while N != 0:
    answer += digit*(N & 1)
    N = N >> 1
    digit *= 3

print(answer)

