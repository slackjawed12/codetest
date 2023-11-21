import sys

T = int(sys.stdin.readline().strip())
answer = []
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    first_pub, second_pub, encrypted = [sys.stdin.readline().strip().split() for _ in range(3)]
    f_dict = {w: i for i, w in enumerate(first_pub)}
    s_dict = {w: i for i, w in enumerate(second_pub)}
    transition_info = {start[1]: f_dict[start[0]] for start in s_dict.items()}
    result = [''] * n
    for i in range(n):
        result[transition_info[i]] = encrypted[i]

    answer.append(result)

for ans in answer:
    print(*ans)