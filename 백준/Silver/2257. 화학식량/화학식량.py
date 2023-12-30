expr = input()

st = []
answer = 0


def value_of(symbol):
    if symbol == 'H':
        return 1
    elif symbol == 'C':
        return 12
    else:
        return 16


for c in list(expr):
    if c == '(':
        st.append(c)
    elif c == ')':
        cur_value = 0
        while st[len(st)-1] != '(':
            last = st.pop()
            cur_value += last
        st.pop()
        st.append(cur_value)
    elif c == 'H' or c == 'C' or c == 'O':
        st.append(value_of(c))
    else:
        multiplier = int(c)
        last = st.pop()
        st.append(last * multiplier)

print(sum(st))