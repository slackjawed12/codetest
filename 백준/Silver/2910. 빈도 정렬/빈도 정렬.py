import sys

N, C = list(map(int, sys.stdin.readline().strip().split()))
message_input = list(map(int, sys.stdin.readline().strip().split()))

store = {}
for index, number in enumerate(message_input):
    if number in store:
        store[number]['count'] += 1
    else:
        store[number] = {'count': 1, 'first': index}

message_input.sort(key=lambda x: (-store[x]['count'], store[x]['first']))
print(*message_input)
