import sys

cards = [sys.stdin.readline().strip().split() for _ in range(5)]


def calculate_score(cards):
    num_store = {}
    color_store = {}
    for card in cards:
        num_store[card[1]] = num_store[card[1]] + 1 if card[1] in num_store else 1
        color_store[card[0]] = color_store[card[0]] + 1 if card[0] in color_store else 1

    is_flush = len(color_store.keys()) == 1
    number_sorted = sorted(cards, key=lambda x: x[1])
    is_straight = len(num_store.keys()) == 5 and int(number_sorted[-1][1]) - int(number_sorted[0][1]) == 4
    counts = num_store.values()
    if is_flush and is_straight:
        nums = list(map(lambda x: int(x[1]), cards))
        return 900 + max(nums)
    elif 4 in counts:
        num = 0
        for n in num_store.keys():
            if num_store[n] == 4:
                num = int(n[0])
        return 800 + num
    elif 3 in counts and 2 in counts:
        three = [int(n) for n in num_store.keys() if num_store[n] == 3][0]
        two = [int(n) for n in num_store.keys() if num_store[n] == 2][0]
        return 700 + three * 10 + two
    elif is_flush:
        return 600 + int(number_sorted[-1][1])
    elif is_straight:
        return 500 + int(number_sorted[-1][1])
    elif 3 in counts:
        num = int([n for n in num_store.keys() if num_store[n] == 3][0])
        return 400 + num
    elif len([x for x in counts if x == 2]) == 2:
        nums = sorted(list(map(int, [n for n in num_store.keys() if num_store[n] == 2])))
        return 300 + nums[-1] * 10 + nums[0]
    elif 2 in counts:
        num = int([n for n in num_store.keys() if num_store[n] == 2][0])
        return 200 + num
    else:
        return 100 + int(number_sorted[-1][1])


print(calculate_score(cards))