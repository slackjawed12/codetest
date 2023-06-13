def run(num, left, right, ans) -> int:
    if (left + 1) // 2 == (right + 1) // 2:
        return ans
    else:
        return run(num // 2, (left + 1) // 2, (right + 1) // 2, ans) + 1


N, a, b = map(int, open(0).read().split())
answer = run(N, a, b, 1)
print(answer)
