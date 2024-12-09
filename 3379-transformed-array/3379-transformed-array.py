class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            if n == 0:
                result.append(n)
            else:
                result.append(nums[(i+n)%len(nums)])

        return result
    