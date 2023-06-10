erased = list(open(0).read().strip())

cur = 1
source = '1'
i, j = 0, 0
while i < len(erased):
    while j < len(source) and erased[i] != source[j]:
        j += 1

    if j != len(source):  # 같은 자리수 있음
        i += 1
        j += 1  # 다음 것과 비교하도록 인덱스 이동
    else:
        j = 0
        cur += 1
        source = str(cur)

print(cur)