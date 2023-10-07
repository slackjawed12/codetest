import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
dna_array = [sys.stdin.readline().strip() for _ in range(N)]

count_list = []
for i in range(M):
    count = {}
    for dna in dna_array:
        if dna[i] in count:
            count[dna[i]] += 1
        else:
            count[dna[i]] = 1

    count_list.append(count)

result_string = []
result_sum = 0
for c in count_list:
    items = list(c.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    result_string.append(items[0][0])
    sliced = items[1:]
    if len(sliced) > 0:
        result_sum += sum([pair[1] for pair in sliced])

print("".join(result_string))
print(result_sum)