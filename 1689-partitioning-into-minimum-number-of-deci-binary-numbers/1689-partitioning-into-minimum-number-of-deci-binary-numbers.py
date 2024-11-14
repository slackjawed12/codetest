class Solution:
    def minPartitions(self, n: str) -> int:
        nums = [int(c) for c in n]
        return max(nums)