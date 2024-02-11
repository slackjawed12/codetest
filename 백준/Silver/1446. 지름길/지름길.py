import sys


def main():
    n, d, infos = input_data()
    answer = get_min_distance(infos, d)
    print(answer)


def input_data():
    n, d = list(map(int, sys.stdin.readline().strip().split()))
    infos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    return n, d, infos


def get_min_distance(info_list: list, target):
    dp = [-1] * (target + 1)
    dp[0] = 0
    shortcuts = {info[1]: [] for info in info_list}
    for info in info_list:
        shortcuts[info[1]].append({'node': info[0], 'dist': info[2]})

    for i in range(1, target + 1):
        if i in shortcuts:
            for shortcut in shortcuts[i]:
                before, dist = shortcut['node'], shortcut['dist']
                dp[i] = min(dp[before] + dist, dp[i]) if dp[i] != -1 else dp[before] + dist

        dp[i] = min(dp[i], dp[i - 1] + 1) if dp[i] != -1 else dp[i - 1] + 1

    return dp[target]


main()
