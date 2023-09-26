import sys

n, *inputs = sys.stdin.read().split()

inputs = [int(x[::-1]) for x in inputs]

inputs.sort()

for t in inputs:
    print(t)
