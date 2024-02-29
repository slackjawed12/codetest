import sys


def get_operation_count(s):
    st = []
    for bracket in list(s):
        if bracket == '{':
            st.append(bracket)
            continue

        if len(st) == 0:
            st.append(bracket)
        else:
            last = st.pop()
            if last != '{':
                st.append(last)
                st.append(bracket)

    result = 0
    for i in range(0, len(st), 2):
        if st[i] == '}' and st[i+1] == '{':
            result += 2
        else:
            result += 1

    return result


answer = []
while True:
    s = sys.stdin.readline().strip()
    num = 1
    if s.count('-') > 0:
        break

    answer.append(get_operation_count(s))

for index, a in enumerate(answer):
    print(str(index + 1) + ".", a)
