import sys
from functools import reduce

S, K = list(map(int, sys.stdin.readline().strip().split()))
numbers = [(S // K) if i >= S % K else (S // K) + 1 for i in range(K)]
answer = reduce(lambda acc, cur: acc * cur, numbers, 1)
print(answer)
