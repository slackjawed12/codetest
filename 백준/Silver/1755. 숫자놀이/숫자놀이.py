import sys

M, N = list(map(int, sys.stdin.readline().strip().split()))
num_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
            9: "nine"}


def convert_number_to_english(num):
    num_list = list(str(num))
    return " ".join([num_dict[int(n)] for n in num_list])


result = [(convert_number_to_english(i), i) for i in range(M, N + 1)]
result.sort(key=lambda t: t[0])

answer = list(map(lambda x: x[1], result))
i = 0
while i < len(result):
    print(*answer[i:i + 10])
    i += 10
