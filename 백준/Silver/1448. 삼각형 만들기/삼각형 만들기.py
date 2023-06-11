N, *arr = map(int, open(0).read().split())
arr.sort()

tri = [int(arr[i]) for i in range(3)]
answer = 0
if tri[0] + tri[1] <= tri[2]:
    answer = -1
else:
    answer = sum(tri)

for num in arr[3:]:
    tri[0] = num
    tri.sort()
    if tri[0] + tri[1] > tri[2]:
        answer = sum(tri)

print(answer)