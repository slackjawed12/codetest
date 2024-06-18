class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(key=lambda x:-x)
        result = 0
        i = 0
        while i < len(cost):
            result += cost[i] 
            if i+1 < len(cost):
                result += cost[i+1]
            i += 3
            
        return result