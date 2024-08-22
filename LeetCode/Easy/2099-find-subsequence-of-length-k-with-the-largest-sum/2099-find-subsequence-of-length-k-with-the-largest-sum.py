class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        temp = sorted(enumerate(nums), key=lambda x:x[1], reverse=True)
        result = temp[:k]
        result.sort(key=lambda x:x[0])
        return [x[1] for x in result]