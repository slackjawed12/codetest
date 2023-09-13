import sys

N = int(input())
votes = []
for _ in range(N):
    votes.append(list(map(int, sys.stdin.readline().strip().split())))

result = [{"num": i + 1, "vote": 0, 3: 0, 2: 0, 1: 0} for i in range(3)]
for vote in votes:
    for index, val in enumerate(vote):
        result[index]["vote"] += val
        result[index][val] += 1

result.sort(key=lambda x: x["vote"])

if result[2]['vote'] != result[1]['vote']:
    print(result[2]['num'], result[2]['vote'])
elif result[2][3] != result[1][3]:
    r = result[2] if result[2][3] > result[1][3] else result[1]
    print(r['num'], r['vote'])
elif result[2][2] != result[1][2]:
    r = result[2] if result[2][2] > result[1][2] else result[1]
    print(r['num'], r['vote'])
else:
    print(0, result[2]['vote'])
