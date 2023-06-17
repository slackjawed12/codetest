N, *req, M = map(int, open(0).read().split())

if sum(req) <= M:
    print(max(req))
else:
    low, high = 1, max(req)
    mid = (low + high) // 2
    while low <= high:
        mid = (low + high) // 2
        mapped = list(map(lambda x: min(mid, x), req))
        temp = sum(mapped)
        if temp < M:
            low = mid + 1
        elif temp > M:
            high = mid - 1
        else:
            high = mid
            break

    print(high)
