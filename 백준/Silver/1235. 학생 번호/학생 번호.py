from collections import Counter

N = int(input())
nums = []
for _ in range(N):
    nums.append(input())

k = 1
length = len(nums[0])
for i in range(1, length + 1):
    count = Counter(list(map(lambda x: x[-i:], nums)))
    if len(count) == N:
        print(i)
        break