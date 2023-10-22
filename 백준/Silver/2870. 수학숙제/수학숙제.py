import sys
import re
N = int(sys.stdin.readline().strip())
lines = [sys.stdin.readline().strip() for _ in range(N)]
numbers = []
for line in lines:
    pattern = re.compile('[0-9]+')
    matched = pattern.findall(line)
    numbers += list(map(int, matched))

numbers.sort()

for n in numbers:
    print(n)

