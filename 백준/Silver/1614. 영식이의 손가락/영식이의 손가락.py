import sys

wounded = int(sys.stdin.readline().strip())
max_count = int(sys.stdin.readline().strip())

answer = 0
if wounded == 1:
    answer = max_count * 8
elif wounded == 5:
    answer = max_count * 8 + 4
else:
    loop, rem = divmod(max_count, 2)
    if wounded == 2:
        answer = loop * 8 + (1 if rem == 0 else 7)
    elif wounded == 3:
        answer = loop * 8 + (2 if rem == 0 else 6)
    else:
        answer = loop * 8 + (3 if rem == 0 else 5)

print(answer)
