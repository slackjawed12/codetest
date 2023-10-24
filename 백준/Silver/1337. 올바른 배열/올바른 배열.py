import sys

N = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

answer = 5
store = {x: 1 for x in nums}
for n in nums:
    cur = sum([1 if i not in store else 0 for i in range(n, n + 5)])
    answer = min(cur, answer)

print(answer)