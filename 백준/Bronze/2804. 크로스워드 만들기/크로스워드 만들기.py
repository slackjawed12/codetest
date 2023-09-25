import sys

A, B = sys.stdin.readline().strip().split()

index_info = []
list_B = list(B)
for index, c in enumerate(list(A)):
    if c in list_B:
        index_info = [list_B.index(c), index]
        break


result = [['.']*len(A) for _ in range(len(B))]

for i in range(len(B)):
    result[i][index_info[1]] = B[i]

for j in range(len(A)):
    result[index_info[0]][j] = A[j]

for k in range(len(result)):
    print("".join(result[k]))