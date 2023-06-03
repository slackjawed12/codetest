a, b = map(int, input().split())

rows = []

for i in range(a):
    rows.append(''.join(reversed(input())))

for s in rows:
    print(s)