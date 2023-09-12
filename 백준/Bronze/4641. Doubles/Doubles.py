import sys

lists = []
while True:
    lists.append(list(map(int, sys.stdin.readline().strip().split())))
    if len(lists[-1]) == 1:
        break

lists = lists[:-1]

result = []
for nums in lists:
    temp = 0
    for num in nums[:-1]:
        temp = temp + 1 if num * 2 in nums else temp

    result.append(temp)

for r in result:
    print(r)