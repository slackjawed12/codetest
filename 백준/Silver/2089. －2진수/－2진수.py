N = int(input())

result = []
while N != 0:
    div, mod = divmod(N, -2)
    if mod == -1:
        mod += 2
        div += 1

    result.append(str(mod))
    N = div

if len(result) == 0:
    print("0")

print("".join(list(reversed("".join(result)))))
