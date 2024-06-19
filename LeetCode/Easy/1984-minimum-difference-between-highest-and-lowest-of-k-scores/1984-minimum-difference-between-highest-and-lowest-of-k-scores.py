class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        result = -1
        for i in range(len(nums)-k+1):
            low, high = nums[i], nums[i+k-1]
            if result == -1:
                result = high - low
            else:
                result = min(result, high-low)

        return result

class Solution2:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))