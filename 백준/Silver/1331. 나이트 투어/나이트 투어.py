visit = [[0] * 6 for _ in range(6)]
d = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

info = []
for i in range(36):
    info.append(input())

pos = (ord(info[0][0]) - ord('A'), 6 - (ord(info[0][1]) - ord('0')))
first = (ord(info[0][0]) - ord('A'), 6 - (ord(info[0][1]) - ord('0')))
visit[pos[1]][pos[0]] = 1
count = 1
for i in range(1, 36):
    np = (ord(info[i][0]) - ord('A'), 6 - (ord(info[i][1]) - ord('0')))
    for j in range(8):
        cmp = (pos[0] + d[j][0], pos[1] + d[j][1])
        if 0 <= cmp[0] < 6 and 0 <= cmp[1] < 6 and cmp == np and visit[np[1]][np[0]] == 0:
            visit[np[1]][np[0]] = 1
            count = count + 1
    pos = np

if count == 36:
    ret = False
    for j in range(8):
        cmp = (pos[0] + d[j][0], pos[1] + d[j][1])
        if 0 <= cmp[0] < 6 and 0 <= cmp[1] < 6 and cmp == first:
            ret = True
            break

    if ret:
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')
