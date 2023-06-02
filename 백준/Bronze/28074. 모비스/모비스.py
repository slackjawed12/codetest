mobis = 'MOBIS'
i = input()
flag = True
for x in mobis:
    if x not in i:
        print("NO")
        flag = False
        break

if flag:
    print("YES")
