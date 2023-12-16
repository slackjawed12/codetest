import sys

N = int(sys.stdin.readline().strip())
pillars = [list(map(int, (sys.stdin.readline().strip().split()))) for _ in range(N)]

pillars.sort(key=lambda x: x[0])

first_highest = max(pillars, key=lambda x: x[1])
last_highest = max(reversed(pillars), key=lambda x: x[1])

result = 0
ascending = []
for i in range(N):
    if len(ascending) == 0:
        ascending.append(pillars[i])
    elif ascending[-1][1] < pillars[i][1]:
        ascending.append(pillars[i])

reverse_ascending = []
for i in reversed(range(N)):
    if len(reverse_ascending) == 0:
        reverse_ascending.append(pillars[i])
    elif reverse_ascending[-1][1] < pillars[i][1]:
        reverse_ascending.append(pillars[i])

for j in range(len(ascending[:-1])):
    result += (ascending[j + 1][0] - ascending[j][0]) * ascending[j][1]

for j in reversed(range(len(reverse_ascending[:-1]))):
    result += (-reverse_ascending[j + 1][0] + reverse_ascending[j][0]) * reverse_ascending[j][1]

result += (last_highest[0] - first_highest[0] + 1) * first_highest[1]
print(result)
