K = int(input())


def get_smallest_size(num):
    is_pow_of_two = num & (num - 1) == 0
    if is_pow_of_two:
        return num
    else:
        result = 1
        while num > 0:
            result *= 2
            num //= 2
        return result


def get_split_count(size, target):
    result = 0
    while target > 0:
        if size > target:
            size //= 2
            result += 1
        else:
            target -= size

    return result


size = get_smallest_size(K)
count = get_split_count(size, K)

print(size, count)
