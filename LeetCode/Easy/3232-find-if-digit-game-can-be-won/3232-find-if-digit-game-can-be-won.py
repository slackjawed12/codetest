class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        total = sum(nums)
        single = sum([n for n in nums if n <= 9])
        return single != total-single