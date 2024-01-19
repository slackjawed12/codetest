import sys
import re

N = int(sys.stdin.readline().strip())
patterns = [sys.stdin.readline().strip() for _ in range(N)]

regex = re.compile("(100+1+|01)+")
result = ["NO" if regex.fullmatch(pattern) is None else "YES" for pattern in patterns]
for r in result:
    print(r)

