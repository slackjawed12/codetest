class Solution:
    def smallestNumber(self, n: int) -> int:
        # 1 - 1
        # 2, 3 - 3
        # 4, 5, 6, 7 - 7
        # 8 ~ 15 - 15
        cnt = 0
        while n:
            cnt += 1
            n = n >> 1
        
        return 2**cnt -1
