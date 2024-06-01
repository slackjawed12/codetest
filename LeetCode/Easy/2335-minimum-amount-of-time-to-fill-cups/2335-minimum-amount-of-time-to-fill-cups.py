class Solution:
    def fillCups(self, amount: list[int]) -> int:
        result = 0
        amount.sort(reverse=True)
        while amount[0] != 0:
            amount[0] -= 1
            if amount[1] > 0:
                amount[1] -= 1

            amount.sort(reverse=True)
            result += 1
        
        return result


import heapq
# using heap solution
class SolutionV2:
    def fillCups(self, amount: list[int]) -> int:
        amount = [-a for a in amount]
        heapq.heapify(amount)
        res = 0
        while True:
            first = heapq.heappop(amount)
            second = heapq.heappop(amount)
            if not first and not second:
                break
            heapq.heappush(amount, first+1) if first else heapq.heappush(amount, first)
            heapq.heappush(amount, second+1) if second else heapq.heappush(amount, second)
            res += 1
        return res