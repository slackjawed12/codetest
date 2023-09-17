N = int(input())

print(0 if N <= 3 else N*(N-1)*(N-2)*(N-3)//24)