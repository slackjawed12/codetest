import sys
from collections import Counter
cases = sys.stdin.read().strip().split('\n')

result = []
for case in cases:
    start, end = [int(x) for x in case.split()]
    count = 0
    for num in range(start, end + 1):
        cnt = Counter(list(str(num)))
        if len([x for x in list(cnt.values()) if x > 1]) >= 1:
            continue
        else:
            count += 1

    result.append(count)

for x in result:
    print(x)
