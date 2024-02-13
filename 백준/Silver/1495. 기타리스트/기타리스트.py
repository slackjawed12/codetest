import sys


def input_data():
    n, s, m = list(map(int, sys.stdin.readline().strip().split()))
    volumes = list(map(int, sys.stdin.readline().strip().split()))
    return [n, s, m, volumes]


def get_max_volume(arr: list, start: int, target: int):
    dp = [[0] * (target + 1) for _ in range(len(arr) + 1)]
    dp[0][start] = 1
    for i in range(len(arr)):
        for j in range(target + 1):
            if dp[i][j] == 1:
                if j + arr[i] <= target:
                    dp[i + 1][j + arr[i]] = 1
                if j - arr[i] >= 0:
                    dp[i + 1][j - arr[i]] = 1

    answer = -1
    for i in range(target, -1, -1):
        if dp[len(arr)][i] == 1:
            answer = i
            break

    return answer


def main():
    n, s, m, volumes = input_data()
    answer = get_max_volume(volumes, s, m)
    print(answer)


main()
