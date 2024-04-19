class Solution:
    def averageValue(self, nums: list[int]) -> int:
        target = [n for n in nums if n % 3 == 0 and n % 2 == 0]
        return sum(target)//(len(target) if len(target) !=0 else 1)