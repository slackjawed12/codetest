class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0
        for n in range(left, right+1):
            set_bits = 0
            tmp = n
            while tmp:
                if tmp % 2:
                    set_bits += 1
                tmp = tmp >> 1

            result += 1 if self.prime(set_bits) else 0
            
        return result
    
    def prime(self, n:int)->bool:
        if n == 1:
            return False

        i = 2
        while i * i <= n:
            if not n % i:
                return False
            i += 1
        
        return True