class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        result = 0
        for i in range(len(nums)):
            a, b = nums[i][i], nums[i][len(nums)-i-1]
            if self.isPrime(a):
                result = max(a, result)
            if self.isPrime(b):
                result = max(b, result)
        
        return result

    def isPrime(self, num) -> bool:
        if num == 1:
            return False

        i=2
        while i*i <= num:
            if num % i == 0:
                return False
            
            i += 1
        
        return True

class Solution2:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def is_prime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return n >= 2
        n = len(nums)
        ans = 0
        for i, row in enumerate(nums):
            for x in [row[i], row[n-1-i]]:
                # 두 번 체크하지 않으므로 더 빠르다
                if x > ans and is_prime(x):
                    ans = x
        return ans
