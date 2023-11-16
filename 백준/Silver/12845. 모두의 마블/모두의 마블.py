import sys

N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))
cards.sort(reverse=True)
level = cards[0]
result = 0
for cur in cards[1:]:
    result += level + cur

print(result)