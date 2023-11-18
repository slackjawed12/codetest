# 팰린드롬 만들기
import sys

str = sys.stdin.readline().strip()


def make_palindrome(string):
    if not is_palindrome(string):
        return "I'm Sorry Hansoo"

    sorted_str = sorted(list(string))
    counter = get_counter(string)

    last, first_half, second_half = "", [], []
    for s in sorted(list(counter)):
        character_list = [x for x in sorted_str if x == s]
        first_half += character_list[:len(character_list) // 2]
        second_half += character_list[len(character_list) // 2:]
        if len(character_list) % 2 == 1:
            last = second_half.pop()

    return "".join(first_half) + last + "".join(reversed(second_half))


def is_palindrome(string):
    counter = get_counter(string)

    if len(string) % 2 == 0:
        result = len([x for x in counter.values() if x % 2 == 1]) == 0
    else:
        result = len([x for x in counter.values() if x % 2 == 1]) == 1

    return result


def get_counter(string):
    counter = {}
    for s in list(string):
        if s in counter:
            counter[s] += 1
        else:
            counter[s] = 1
    return counter


print(make_palindrome(str))
