import sys

N = int(sys.stdin.readline().strip())
expected_ranks = [int(sys.stdin.readline().strip()) for _ in range(N)]

expected_ranks.sort()
answer = sum([abs(index+1-rank) for index, rank in enumerate(expected_ranks)])

print(answer)