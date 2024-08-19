class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result = 0
        i = 0
        while tickets[k]:
            if tickets[i] > 0:
                tickets[i] -= 1
                result += 1

            i = (i+1)%len(tickets)

        return result

# optimized O(n)
class Solution2:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result = 0
        for i in range(len(tickets)):
            if i <= k:
                result += min(tickets[i], tickets[k])
            else:
                result += min(tickets[i], tickets[k]-1)

        return result