from collections import defaultdict

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        cnt = defaultdict(int)
        for d in digits:
            cnt[d] += 1
        
        result = []
        for i in range(100, 1000, 2):
            temp = i
            t_cnt = defaultdict(int)
            while temp > 0:
                t_cnt[temp%10] += 1
                temp //= 10

            is_included = True
            for k, v in t_cnt.items():
                if cnt[k] < v:
                    is_included = False
                    break
            
            if is_included:
                result.append(i)

        return result
            
        