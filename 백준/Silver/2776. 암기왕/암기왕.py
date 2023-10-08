import sys

T = int(sys.stdin.readline().strip())

answer = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    diary_one = set(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    diary_two = list(map(int, sys.stdin.readline().strip().split()))
    result = ["1" if num in diary_one else "0" for num in diary_two]
    answer.append("\n".join(result))

for a in answer:
    print(a)