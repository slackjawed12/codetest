import sys


def input_data():
    sl, sr = sys.stdin.readline().strip().split()
    target = sys.stdin.readline().strip()
    return [sl, sr, target]


def get_min_time(l, r, s: str):
    l_pos, r_pos = l, r
    keyboard = [list("qwertyuiop"), list("asdfghjkl"), list("zxcvbnm")]
    key_dict = {}
    for i, row in enumerate(keyboard):
        for j, c in enumerate(row):
            key_dict[c] = {'x': j, 'y': i}

    vowels = set(list("yuiophjklbnm"))
    result = 0
    for i in range(len(s)):
        if s[i] in vowels:
            taxi_dist = abs(key_dict[r_pos]['x'] - key_dict[s[i]]['x']) + abs(
                key_dict[r_pos]['y'] - key_dict[s[i]]['y'])
            result += taxi_dist + 1
            r_pos = s[i]
        else:
            taxi_dist = abs(key_dict[l_pos]['x'] - key_dict[s[i]]['x']) + abs(
                key_dict[l_pos]['y'] - key_dict[s[i]]['y'])
            result += taxi_dist + 1
            l_pos = s[i]

    return result


li, ri, target_str = input_data()
answer = get_min_time(li, ri, target_str)
print(answer)
