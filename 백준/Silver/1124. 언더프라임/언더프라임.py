import sys


class Solution:
    def __init__(self):
        self.a, self.b = list(map(int, sys.stdin.readline().strip().split()))

    def under_primes(self):
        start = self.a
        end = self.b
        sheet = [True] * (end + 1)
        sheet[0] = False
        sheet[1] = False
        # era
        for i in range(2, end + 1):
            if sheet[i]:
                cur = i * 2
                while cur < end + 1:
                    sheet[cur] = False
                    cur += i

        answer = [num for num in range(start, end + 1) if self.is_under_prime(num, sheet)]
        return len(answer)

    def is_under_prime(self, num: int, sheet: list):
        if sheet[num]:
            return False

        i = 2
        result = 0
        temp = num
        while i * i <= temp:
            if not sheet[i]:
                i += 1

            while temp % i == 0:
                temp //= i
                result += 1

            i += 1

        if sheet[temp]:
            result += 1

        return sheet[result]


sol = Solution()
print(sol.under_primes())
