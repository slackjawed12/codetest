import sys

number_input = list(map(int, sys.stdin.readline().strip().split()))


def clocknum(nums):
    num_list = []
    length = len(nums)
    for i in range(length):
        cur = []
        for j in range(i, length + i):
            cur.append(str(nums[j % length]))

        num_list.append(int("".join(cur)))

    return min(num_list)


target = clocknum(number_input)
clock_nums = []
order = 0
for num in range(1111, 10000):
    nums_list = list(str(num))
    if '0' in nums_list:
        continue

    cur_clock = clocknum(nums_list)
    if cur_clock not in clock_nums:
        clock_nums.append(cur_clock)

    if cur_clock == target:
        break

print(len(clock_nums))
