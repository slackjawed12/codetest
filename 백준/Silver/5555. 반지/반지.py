import sys

S = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
inputs = [sys.stdin.readline().strip() for _ in range(N)]

result = 0
for line in inputs:
    for i in range(len(line)):
        substr = line[i:len(S)+i] + (line[:i-len(line)+len(S)] if i >= len(line)-len(S) else "")
        if substr == S:
            result += 1
            break

print(result)