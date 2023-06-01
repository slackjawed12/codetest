import sys

one=int(sys.stdin.readline())
car_numbers=list(map(int, sys.stdin.readline().split()))

answer=0

for x in car_numbers:
    if x==one:
        answer+=1

print(answer)