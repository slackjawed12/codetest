class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        s = set(candyType)
        
        return min(len(s), len(candyType)//2)