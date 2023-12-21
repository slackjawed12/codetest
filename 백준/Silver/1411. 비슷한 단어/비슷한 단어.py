import sys

N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]


def is_similar(first, second):
    converted_list = list(first)
    pair = {}
    inverse_pair = {}
    for i in range(len(first)):
        cur_character, mapping_character = converted_list[i], second[i]
        if cur_character not in pair:
            if mapping_character not in inverse_pair:
                pair[cur_character] = mapping_character
                inverse_pair[mapping_character] = cur_character
                converted_list[i] = mapping_character
            else:
                return False
        elif pair[cur_character] != mapping_character:
            return False
        else:
            converted_list[i] = mapping_character

    if "".join(converted_list) == second:
        return True

    return False


answer = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if is_similar(words[i], words[j]):
            answer += 1

print(answer)
