class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        result = 0
        for i in range(len(hours)-1):
            for j in range(i+1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    result += 1
        
        return result

from collections import defaultdict

class Solution2:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        count = defaultdict(int)
        result = 0
        for hour in hours:
            remainder = hour % 24
            if (24 - remainder) % 24 in count:
                result += count[(24 - remainder) % 24]
            count[remainder] += 1

        return result