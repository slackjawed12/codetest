# 덩치
import sys
from typing import List


class Solution:
    def solve(self, info: List[List[int]]) -> List[int]:
        result = [1] * len(info)
        for i in range(len(info)):
            w, h = info[i]
            for j in range(len(info)):
                if i != j and w < info[j][0] and h < info[j][1]:
                    result[i] += 1

        return result


def main():
    N = int(sys.stdin.readline().strip())
    arr = [list(map(int, (sys.stdin.readline().strip().split()))) for i in range(N)]
    sol = Solution()
    answer = sol.solve(arr)
    print(*answer)


if __name__ == '__main__':
    main()
