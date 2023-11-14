import sys

N = int(sys.stdin.readline().strip())
A, B = list(map(int, sys.stdin.readline().strip().split()))
dough = int(sys.stdin.readline().strip())
toppings = [int(sys.stdin.readline().strip()) for _ in range(N)]

toppings.sort(reverse=True)
cur_calorie = dough
cur_price = A
best = dough / A
for cal in toppings:
    cur_calorie += cal
    cur_price += B
    eff = cur_calorie / cur_price
    if eff > best:
        best = eff

print(int(best))
