class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        result = divisors[0]
        mx = 0
        for div in divisors:
            cnt = 0
            for num in nums:
                if num % div == 0:
                    cnt += 1
            
            if mx < cnt:
                result = div
                mx = cnt
            elif mx == cnt:
                result = min(result, div)
        
        return result