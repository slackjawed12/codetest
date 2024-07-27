class Solution:
    def isThree(self, n: int) -> bool:
        i = 1
        result = 0
        while i <= n:
            if n % i == 0:
                result += 1
            
            if result >=4:
                break

            i += 1

        return result == 3